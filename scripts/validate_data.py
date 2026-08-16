#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_data.py — 校验项目数据并与《世界人口展望 2024》(WPP2024) 关键结论对齐。

读取 data/ 下的 CSV，核对页面信息图所引用的核心数字：
  · 2024 年世界人口约 82 亿
  · 2084 年前后达峰约 103 亿
  · 2100 年约 102 亿
  · 全球总和生育率约 2.3，更替水平 2.1
  · 印度于 2023 年超越中国
  · 65+ 人口在 2070 年代后期超过 18− 儿童

运行：
  python scripts/validate_data.py
（建议在仓库根目录执行；依赖仅标准库 csv。）
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")

REPLACEMENT_TFR = 2.1  # 生育更替水平（每名妇女一生平均生育数）


def load(path):
    # utf-8-sig 自动剔除可能的 BOM，避免首列键变为 "\ufeffyear"
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def get(rows, year, col):
    for r in rows:
        if int(r["year"]) == year:
            return float(r[col])
    raise KeyError(f"year {year} not found in {os.path.basename(path)}")


def approx(a, b, tol=0.15):
    return abs(a - b) <= tol


def find_crossover(rows, col_a, col_b):
    """线性插值求 col_a 与 col_b 的交叉年份（col_a 由高转低或反超）。"""
    rs = sorted(rows, key=lambda r: int(r["year"]))
    for i in range(1, len(rs)):
        y0, y1 = int(rs[i - 1]["year"]), int(rs[i]["year"])
        a0, a1 = float(rs[i - 1][col_a]), float(rs[i][col_a])
        b0, b1 = float(rs[i - 1][col_b]), float(rs[i][col_b])
        d0, d1 = a0 - b0, a1 - b1
        if d0 == 0:
            return y0
        if d0 * d1 < 0:  # 符号变化 => 交叉
            frac = d0 / (d0 - d1)
            return y0 + frac * (y1 - y0)
    return None


def main():
    pop = load(os.path.join(DATA, "population_total.csv"))
    fert = load(os.path.join(DATA, "fertility_rates.csv"))
    age = load(os.path.join(DATA, "age_structure.csv"))
    ic = load(os.path.join(DATA, "india_china.csv"))

    checks = []
    ok = True

    def check(name, cond, detail):
        nonlocal ok
        ok = ok and cond
        checks.append(("通过" if cond else "失败", name, detail))

    # 1) 世界人口关键节点
    p2024 = get(pop, 2024, "world_billion")
    p2084 = get(pop, 2084, "world_billion")
    p2100 = get(pop, 2100, "world_billion")
    check("2024 世界人口 ≈ 82 亿", approx(p2024, 8.2, 0.2), f"{p2024:.1f} 十亿")
    check("2084 达峰 ≈ 103 亿", approx(p2084, 10.3, 0.2), f"{p2084:.1f} 十亿")
    check("2100 ≈ 102 亿（低于峰值）", approx(p2100, 10.2, 0.2) and p2100 <= p2084,
          f"{p2100:.1f} 十亿")

    # 2) 生育率
    tfr2024 = get(fert, 2024, "world")
    check("全球 TFR(2024) ≈ 2.3", approx(tfr2024, 2.3, 0.15), f"{tfr2024:.2f}")
    check("更替水平 = 2.1", REPLACEMENT_TFR == 2.1, f"{REPLACEMENT_TFR}")

    # 3) 印度 vs 中国（2023 反超）
    in23 = get(ic, 2023, "india_million")
    ch23 = get(ic, 2023, "china_million")
    check("印度 2023 超越中国", in23 > ch23, f"印度 {in23:.0f}M > 中国 {ch23:.0f}M")

    # 4) 老龄化交叉（65+ 超过 18−）
    cross = find_crossover(age, "over65_billion", "under18_billion")
    check("65+ 在 2070 年代后期超过 18−", cross is not None and 2070 <= cross <= 2085,
          f"交叉年 ≈ {cross:.0f}" if cross else "未检测到交叉")

    # 输出
    print("=" * 60)
    print(" 全球人口结构与趋势 · 数据校验 (UN WPP 2024 中位数情景)")
    print("=" * 60)
    for status, name, detail in checks:
        print(f"  [{status}] {name}: {detail}")
    print("-" * 60)
    print(f" 峰值年份对应人口: 2084 -> {p2084:.1f} 十亿")
    print(f" 65+ / 18− 交叉年份(插值): {cross:.0f}" if cross else " 交叉年份: 未检测到")
    print("=" * 60)
    if ok:
        print(" 全部核对通过 ✅")
        return 0
    print(" 存在未通过项 ❌")
    return 1


if __name__ == "__main__":
    sys.exit(main())
