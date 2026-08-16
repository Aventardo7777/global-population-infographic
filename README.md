<div align="center">

# 🌍 膨胀的星球 · 全球人口结构与趋势

### 一份杂志编辑设计风的单文件数据可视化信息图 · 基于 UN World Population Prospects 2024

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![HTML5](https://img.shields.io/badge/HTML5-Self--contained-E34F26.svg)](#)
[![deps](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](#)
[![data](https://img.shields.io/badge/data-UN%20WPP%202024-2EA44F.svg)](https://population.un.org/wpp/)
[![charts](https://img.shields.io/badge/charts-inline%20SVG-8B5CF6.svg)](#-图表架构)
[![offline](https://img.shields.io/badge/offline-ready-22C55E.svg)](#-快速开始)
[![lang](https://img.shields.io/badge/lang-简体中文-red.svg)](#)

**82 亿 → 103 亿** · 一个增长见顶的星球，正在经历结构重组。<br/>
纯静态、零依赖、零外链 —— 双击 `index.html` 即可离线运行。

</div>

---

> ### 💡 TL;DR
> 把联合国《世界人口展望 2024》中位数情景，变成一张**会呼吸的杂志信息图**：
> 航拍城市 Hero + 彩色色块拼贴、超大数字指标墙、四张内联 SVG 图表（人口达峰 / 生育率 / 老龄化交叉 / 印中易主），
> 全部坐标经裁剪**绝不溢出坐标轴**。配套 CSV 数据 + Python 校验脚本，结论可一键复现。

---

## 📑 目录

- [✨ 项目亮点](#-项目亮点)
- [📊 一图读懂：六个关键数字](#-一图读懂六个关键数字)
- [🚀 快速开始](#-快速开始)
- [🧩 板块与图表一览](#-板块与图表一览)
- [🏗️ 图表架构](#️-图表架构)
- [🎨 设计系统](#-设计系统)
- [📁 项目结构](#-项目结构)
- [📈 数据校验](#-数据校验)
- [🔧 自定义指南](#-自定义指南)
- [🛣️ 路线图](#️-路线图)
- [❓ FAQ](#-faq)
- [🤝 贡献](#-贡献)
- [📜 许可证与数据归属](#-许可证与数据归属)
- [🙏 致谢](#-致谢)

---

## ✨ 项目亮点

| | 特性 | 说明 |
| --- | --- | --- |
| 📦 | **真正的单文件** | `index.html` 内联全部 CSS / JS 与两张配图（base64），**无任何外链**，离线可用 |
| 🎨 | **杂志信息图风** | 明亮大胆、强对比大色块、超大数字排版、图片裁成色块拼贴 |
| 📈 | **纯 SVG 图表** | 四张图表全部手写 SVG，坐标裁剪 + clipPath 双重保险，不溢出坐标轴 |
| 🌐 | **简体中文界面** | 面向中文读者的叙事化数据故事 |
| 🔬 | **可复现** | `data/` 下 CSV 与图表一一对应，`scripts/validate_data.py` 一键核对关键结论 |
| 🪶 | **零依赖** | 无 npm、无构建步骤、无框架——浏览器即运行时 |
| ♿ | **可访问性** | 图表带 `role="img"` / `aria-label`，每个数据点含 `<title>` 原生提示 |

---

## 📊 一图读懂：六个关键数字

> 以下指标均来自联合国《世界人口展望 2024》**中位数情景（medium variant）**。

| 指标 | 数值 | 含义 |
| :--- | :---: | :--- |
| 2024 年世界人口 | **≈ 82 亿** | 较 1950 年的 25 亿增长逾 3 倍 |
| 预计峰值（≈2084 年） | **≈ 103 亿** | 本世纪下半叶触顶后趋于稳定 |
| 2100 年 | **≈ 102 亿** | 略低于峰值，进入“平台化” |
| 全球总和生育率（TFR） | **≈ 2.3** | 每名妇女平均生育数，持续下行 |
| 生育更替水平 | **2.1** | 低于此值且无移民补充，长期人口将萎缩 |
| 印度超越中国 | **2023 年** | 头号人口大国易主 |
| 65+ 超过 18− | **2070 年代后期** | “银发时代”正式到来（插值交叉 ≈ 2073） |

---

## 🚀 快速开始

无需安装任何东西——三种方式任选：

```bash
# ① 最简单：直接双击 index.html（任意现代浏览器）

# ② 本地静态服务器（推荐，便于调试）
python -m http.server 8080
#   打开 http://localhost:8080

# ③ Node 生态
npx serve .
```

> 🟢 **完全离线**：所有图片已内联为 base64，断网也能 100% 正常显示与交互。

---

## 🧩 板块与图表一览

页面自上而下是一段“数据故事”：

```
┌───────────────────────────────────────────────┐
│  HERO   航拍城市 + 82亿→103亿 叙事             │  色块拼贴 · 超大印章数字
├───────────────────────────────────────────────┤
│  指标墙   六个关键数字（大色块卡片）            │  82亿 / 103亿 / 2.3 / 2.1 / 印超车 / 65+反超
├───────────────────────────────────────────────┤
│  ① 人口达峰曲线        1950→2100，标注 2084 峰值 │  SVG 折线 + 峰值标注
│  ② 多区域生育率折线    世界/非洲/亚洲/欧洲+2.1线 │  SVG 多折线 + 更替虚线
│  ③ 老龄化 65+ vs 18−   交叉点 ≈ 2073            │  SVG 双折线 + 交叉标注
│  ④ 印度 vs 中国        2023 交叉                 │  SVG 双折线 + 反超标注
├───────────────────────────────────────────────┤
│  区域增长分化          非洲/亚洲/欧洲/拉美/北美/大洋洲 │  色块卡片 + 人群配图拼贴
├───────────────────────────────────────────────┤
│  来源与建模说明        WPP2024 口径 / 局限 / 复现 │  页脚
└───────────────────────────────────────────────┘
```

---

## 🏗️ 图表架构

四张图共用一个通用渲染器 `lineChart(cfg)`，核心是**“映射 + 裁剪 + 裁剪盒”三重防溢出**：

```js
// 1) 固定逻辑坐标系（viewBox），外层 CSS width:100% 实现响应式
//    <svg viewBox="0 0 W H" preserveAspectRatio="xMidYMid meet">

// 2) 线性映射：数据 -> 像素
const sx = x => padL + (x - xMin) / (xMax - xMin) * plotW;
const sy = y => H - padB - (y - yMin) / (yMax - yMin) * plotH;

// 3) 坐标裁剪：任何点都夹取到绘图区内 —— 杜绝溢出坐标轴
const clampX = x => Math.max(padL, Math.min(W - padR, sx(x)));
const clampY = y => Math.max(padT, Math.min(H - padB, sy(y)));

// 4) 双重保险：clipPath 矩形 = 绘图区
//    <g clip-path="url(#clip)"> …所有折线与圆点… </g>
```

**为什么这样设计？**
- 即便输入了越界数据，曲线也不会画出坐标轴之外；
- 峰值点 / 交叉点等**标注文字**位置同样被 `clamp`，避免与坐标轴或边框重叠；
- `viewBox` + `preserveAspectRatio` 保证任意屏幕宽度下不变形、不裁切。

> 想加第五张图？只需往 `DATA` 对象里加一段配置，调用一次 `lineChart({...})` 即可，无需改渲染器。

---

## 🎨 设计系统

CSS 自定义属性集中在 `:root`，统一管控全站视觉：

| 变量 | 色值 | 用途 | 色样 |
| --- | --- | --- | --- |
| `--ink` | `#15110E` | 近黑墨色（正文 / 轴线） | ![](https://img.shields.io/badge/%2315110E-墨-15110E.svg) |
| `--paper` | `#F6F1E7` | 暖米色背景 | ![](https://img.shields.io/badge/%23F6F1E7-纸-F6F1E7.svg) |
| `--red` | `#E8392B` | 主强调（峰值 / 中国 / 65+） | ![](https://img.shields.io/badge/%23E8392B-红-E8392B.svg) |
| `--blue` | `#1347C9` | 次强调（世界 / 18− / 印度） | ![](https://img.shields.io/badge/%231347C9-蓝-1347C9.svg) |
| `--yellow` | `#FFC400` | 高亮色块 / 印章 | ![](https://img.shields.io/badge/%23FFC400-黄-FFC400.svg) |
| `--teal` | `#0E9C8A` | 欧洲系列 | ![](https://img.shields.io/badge/%230E9C8A-青-0E9C8A.svg) |
| `--magenta` | `#D3297A` | 印度系列 | ![](https://img.shields.io/badge/%23D3297A-洋红-D3297A.svg) |
| `--orange` | `#F26419` | 非洲系列 | ![](https://img.shields.io/badge/%23F26419-橙-F26419.svg) |

**排版哲学**：超大数字用 `font-weight:900` + `clamp()` 流式缩放；Hero 用航拍图叠加半透明色块（`mix-blend-mode:multiply`）拼贴；关键结论用黑色卡片 + 黄色左边框强调——让数字“跳”出来。

---

## 📁 项目结构

```
global-population-infographic/
├── index.html              # ⭐ 自包含信息图（CSS/JS/图片全部内联）
├── README.md               # 本文件
├── LICENSE                 # MIT
│
├── assets/                 # AI 生成配图的原始 PNG（页面已内联，仅作溯源）
│   ├── A_dramatic_high_angle_aerial_*.png     # Hero 航拍城市
│   └── A_diverse_colorful_crowd_*.png         # 区域板块人群
│
├── data/                   # 与页面图表一一对应的 CSV
│   ├── population_total.csv    # 01 达峰曲线
│   ├── fertility_rates.csv     # 02 生育率
│   ├── age_structure.csv       # 03 老龄化交叉
│   └── india_china.csv         # 04 印中交叉
│
├── scripts/
│   ├── validate_data.py        # 🔬 校验关键数字，输出核对摘要
│   └── _make_inline_images.py  # 🛠️ 将配图压缩为内联 base64（构建用）
│
└── docs/
    └── methodology.md          # 📖 数据口径与图表绘制/防溢出机制
```

---

## 📈 数据校验

一条命令，核对全部关键结论是否与 WPP2024 一致：

```bash
python scripts/validate_data.py
```

典型输出：

```
============================================================
 全球人口结构与趋势 · 数据校验 (UN WPP 2024 中位数情景)
============================================================
  [通过] 2024 世界人口 ≈ 82 亿: 8.2 十亿
  [通过] 2084 达峰 ≈ 103 亿: 10.3 十亿
  [通过] 2100 ≈ 102 亿（低于峰值）: 10.2 十亿
  [通过] 全球 TFR(2024) ≈ 2.3: 2.30
  [通过] 更替水平 = 2.1: 2.1
  [通过] 印度 2023 超越中国: 印度 1429M > 中国 1425M
  [通过] 65+ 在 2070 年代后期超过 18−: 交叉年 ≈ 2073
------------------------------------------------------------
 峰值年份对应人口: 2084 -> 10.3 十亿
 65+ / 18− 交叉年份(插值): 2073
============================================================
 全部核对通过 ✅
```

> 脚本仅依赖 Python 标准库 `csv`，无需安装第三方包。
> 老龄化交叉年用**线性插值**自动求解，改了数据也会自动重算。

---

## 🔧 自定义指南

| 想改什么 | 改哪里 |
| --- | --- |
| 图表数值 | `data/*.csv`，再跑 `validate_data.py` 核对 |
| 配色 / 字体 | `index.html` 顶部 `:root` 的 CSS 变量 |
| 增删图表 | `<script>` 中 `DATA` 对象 + 一次 `lineChart({...})` 调用 |
| 替换配图 | 把新图放进 `assets/`，改 `scripts/_make_inline_images.py` 文件名后重跑 |
| 增加区域卡片 | HTML 中 `.regions` 网格里加一个 `.reg` 色块 |

---

## 🛣️ 路线图

- [x] 单文件自包含信息图（含内联配图）
- [x] 四张防溢出 SVG 图表
- [x] CSV 数据 + Python 校验
- [ ] 暗色主题切换
- [ ] 图表 hover 高亮当前系列
- [ ] 可切换 WPP2024 高/低生育率情景对比
- [ ] 响应式移动端竖排图例优化
- [ ] 嵌入联合国官方数据 API 自动更新

---

## ❓ FAQ

**Q：为什么不用 ECharts / D3 / Chart.js？**
A：本项目的目标是“单文件、零依赖、可离线、杂志级排版”。手写 SVG 能完全掌控坐标裁剪与视觉风格，且产物体积可控。引入图表库会破坏“双击即用”的体验。

**Q：数据是逐年精确值吗？**
A：不是。曲线为 WPP2024 中位数情景下的**示意性插值**，按趋势平滑，用于趋势叙事。精确逐年数据请查阅联合国官方数据库。

**Q：图片有版权问题吗？**
A：配图由 AI 生成并经内联压缩，无外部版权依赖。数据结论归属联合国。

**Q：能在手机上看吗？**
A：可以。页面响应式，移动端会自动单列排版；图表用 `viewBox` 自适应缩放。

---

## 🤝 贡献

欢迎提 Issue / PR！小到错别字、大到新增图表情景，都欢迎：

1. Fork 本仓库
2. 新建分支：`git checkout -b feat/your-feature`
3. 提交：`git commit -m "feat: ..."`
4. 推送：`git push origin feat/your-feature`
5. 发起 Pull Request

请确保 `python scripts/validate_data.py` 仍全部通过。

---

## 📜 许可证与数据归属

- 代码与设计：[MIT License](LICENSE) © 2024 环球人口观察
- **数据来源**：联合国《世界人口展望 2024》(World Population Prospects 2024) —— 数据结论归属联合国，本仓库仅用于教学与科普可视化示例。

---

## 🙏 致谢

- [United Nations, Department of Economic and Social Affairs, Population Division](https://population.un.org/wpp/) — 《世界人口展望 2024》
- 所有推动开放数据与科学传播的人们

---

<div align="center">

**如果这个项目对你有帮助，欢迎 ⭐ Star 支持！**

Made with ❤️ · HTML · SVG · 纯静态 · 零依赖

</div>
