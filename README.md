# 全球人口结构与趋势 · 数据可视化信息图

> 一份杂志编辑设计风（明亮大胆 / 强对比大色块 / 超大数字排版）的单文件交互信息图，
> 基于**联合国《世界人口展望 2024》(World Population Prospects 2024) 中位数情景**的真实数据，
> 讲述“82 亿 → 103 亿”的人口增长与结构转折故事。

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## ✨ 特性

- **单文件自包含**：`index.html` 内含全部 CSS、JS，以及两张已内联（base64）配图——**无任何外部链接**，双击即可离线打开。
- **纯 SVG 图表**：人口达峰曲线、区域生育率折线、老龄化交叉图、印中人口交叉图，全部用内联 SVG 绘制，坐标经裁剪**绝不溢出坐标轴**。
- **杂志信息图风格**：航拍城市 Hero + 彩色色块拼贴、关键数字指标墙、超大数字排版。
- **简体中文界面**。
- **可复现**：所有曲线数值来自 `data/` 下 CSV，配套 `scripts/validate_data.py` 一键核对关键结论。

## 📊 关键数字（UN WPP 2024）

| 指标 | 数值 |
| --- | --- |
| 2024 年世界人口 | ≈ 82 亿 |
| 预计峰值（≈2084 年） | ≈ 103 亿 |
| 2100 年 | ≈ 102 亿 |
| 全球总和生育率（TFR） | ≈ 2.3 |
| 生育更替水平 | 2.1 |
| 印度超越中国 | 2023 年 |
| 65+ 超过 18− | 2070 年代后期 |

## 🚀 本地预览

无需任何依赖，直接用浏览器打开：

```bash
# 方式一：双击
open index.html        # macOS
# Windows: 直接在资源管理器双击 index.html

# 方式二：起一个本地静态服务器（可选）
python -m http.server 8080
# 然后访问 http://localhost:8080
```

## 🗂 目录结构

```
global-population-infographic/
├── index.html              # 自包含信息图页面（CSS/JS/图片全部内联）
├── README.md               # 本文件
├── LICENSE                 # MIT 许可证
├── assets/                 # AI 生成配图的原始 PNG（页面已内联，仅作溯源）
│   ├── A_dramatic_high_angle_aerial_*.png   # Hero 航拍城市
│   └── A_diverse_colorful_crowd_*.png       # 区域板块人群
├── data/                   # 与页面图表一一对应的数据（CSV）
│   ├── population_total.csv
│   ├── fertility_rates.csv
│   ├── age_structure.csv
│   └── india_china.csv
├── scripts/
│   ├── validate_data.py    # 校验关键数字，输出核对摘要
│   └── _make_inline_images.py  # 将配图压缩为内联 base64（构建用）
└── docs/
    └── methodology.md      # 数据口径与图表绘制/防溢出机制说明
```

## 🔬 复现与校验

```bash
python scripts/validate_data.py
```

脚本会读取 `data/` 下 CSV，核对上述所有关键结论（82 亿、峰值 103 亿、TFR 2.3、更替 2.1、2023 印度超车、老龄化交叉年），并打印通过/失败摘要。

## ⚠️ 数据说明

- 曲线为 **WPP2024 中位数情景**下的示意性插值，逐年点来自公开汇总并按趋势平滑，用于趋势叙事，非逐年精确值。
- 区域增长百分比为 2024→2050 的粗略估算，仅作方向性参考。
- 配图由 AI 生成并经内联压缩，无版权外部依赖。

## 📜 许可证

[MIT](LICENSE) · 数据与结论归属联合国《世界人口展望 2024》。
