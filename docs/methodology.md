# 方法论与技术说明（Methodology）

本文档说明 `index.html` 背后的数据口径、SVG 绘制机制与设计系统，便于二次修改与复现。

---

## 1. 数据口径

| 项 | 说明 |
| --- | --- |
| 来源 | 联合国《世界人口展望 2024》(World Population Prospects 2024) |
| 情景 | **中位数情景（medium variant）**——页面所有曲线均基于此 |
| 单位 | 人口 = 十亿；总和生育率(TFR) = 每名妇女一生平均生育子女数；印度/中国 = 百万人 |
| 时间 | 1950–2024 为历史估计，2024 之后为预测 |
| 性质 | 曲线为公开汇总的**示意性插值**，按趋势平滑，用于趋势叙事，非逐年精确值 |

### 关键结论（均已通过 `scripts/validate_data.py` 核对）
- 2024 年世界人口 ≈ 82 亿；2084 年前后达峰 ≈ 103 亿；2100 年 ≈ 102 亿（略低于峰值）。
- 全球 TFR ≈ 2.3；生育更替水平 = 2.1（低于此值且无移民补充，长期人口将萎缩）。
- 印度于 **2023 年**超越中国，成为人口第一大国。
- 65+ 人口与 18− 儿童的交叉年（线性插值）≈ **2073**（即 2070 年代后期）。

---

## 2. 数据文件与图表的映射

| CSV 文件 | 对应页面图表 | 主要字段 |
| --- | --- | --- |
| `data/population_total.csv` | 01 人口达峰曲线 | `year`, `world_billion` |
| `data/fertility_rates.csv` | 02 多区域生育率折线 | `year`, `world`, `africa`, `asia`, `europe` |
| `data/age_structure.csv` | 03 老龄化 65+ vs 18− 交叉 | `year`, `under18_billion`, `over65_billion` |
| `data/india_china.csv` | 04 印度 vs 中国交叉 | `year`, `india_million`, `china_million` |

> 页面 `<script>` 中的 `DATA` 对象与这些 CSV 一一对应；修改数据时，建议直接改 CSV，
> 再跑 `python scripts/validate_data.py` 核对关键数字是否仍成立。

---

## 3. SVG 图表绘制与“防溢出”机制

所有图表由同一个通用渲染器 `lineChart(cfg)` 生成内联 `<svg>`，核心思路：

1. **固定逻辑坐标系（viewBox）**
   `viewBox="0 0 W H"`，内部所有坐标按该坐标系计算；外层 CSS 设 `svg{width:100%;height:auto}`，
   配合 `preserveAspectRatio="xMidYMid meet"` 实现响应式缩放且不变形。

2. **线性映射**
   ```
   sx(x) = padL + (x - xMin)/(xMax - xMin) * plotW
   sy(y) = H - padB - (y - yMin)/(yMax - yMin) * plotH
   ```
   其中 `plotW = W - padL - padR`，`plotH = H - padT - padB`。

3. **坐标裁剪（关键：杜绝溢出坐标轴）**
   ```
   clampX(x) = max(padL, min(W - padR, sx(x)))
   clampY(y) = max(padT, min(H - padB, sy(y)))
   ```
   任何数据点、标注文字的位置都先经过 `clampX/clampY`，确保落在绘图区内。

4. **双重保险：clipPath**
   所有数据系列外层包裹
   `<g clip-path="url(#${id}-clip)">`，`clipPath` 矩形恰好等于绘图区，
   即便极端数据也不会画出边框之外。

5. **标注（peak / 交叉点）位置同样被 clamp**
   峰值点、老龄化交叉点、印中交叉点的文字标签坐标也会被夹取在 `[padL+4, W-padR-4]` 与
   `[padT+14, H-padB-4]` 之间，避免出框或与坐标轴重叠。

6. **可访问性**：每个数据点带 `<title>` 原生提示，图表含 `role="img"` 与 `aria-label`。

---

## 4. 设计系统（杂志信息图风）

CSS 自定义属性集中在 `:root`：

| 变量 | 色值 | 用途 |
| --- | --- | --- |
| `--ink` | `#15110E` | 近黑墨色（正文/轴线） |
| `--paper` | `#F6F1E7` | 暖米色背景 |
| `--red` | `#E8392B` | 主强调（峰值、中国、65+） |
| `--blue` | `#1347C9` | 次强调（世界人口、18−、印度） |
| `--yellow` | `#FFC400` | 高亮色块 / 印章 |
| `--teal` | `#0E9C8A` | 欧洲系列 |
| `--magenta` | `#D3297A` | 印度系列 |
| `--orange` | `#F26419` | 非洲系列 |

设计要点：超大数字用 `font-weight:900` + `clamp()` 流式缩放；Hero 用航拍图 + 半透明
色块（`mix-blend-mode:multiply`）拼贴；关键结论用黑色卡片 + 黄色左边框强调。

---

## 5. 图片内联

- `assets/` 下为 AI 生成的原始 PNG（航拍城市、多元人群），仅作溯源。
- 实际页面中的图片经由 `scripts/_make_inline_images.py` 压缩为 JPEG 并转为 base64
  `data:` URI 直接写入 `index.html`，因此 **index.html 单文件即可离线运行，无外链**。
- 若需替换配图：把新图放进 `assets/`，修改 `_make_inline_images.py` 中的文件名后重跑，
  再用占位符 `__HERO_IMG__` / `__CROWD_IMG__` 注入即可。

---

## 6. 复现步骤

```bash
# 1) 校验数据
python scripts/validate_data.py

# 2) （可选）重建内联图片
python scripts/_make_inline_images.py

# 3) 预览
python -m http.server 8080   # 打开 http://localhost:8080
```
