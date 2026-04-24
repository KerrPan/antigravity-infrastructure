---
name: d2-styler
description: 專業級 D2 語言圖表渲染技能。支援 ELK 佈局引擎，產出極度緊湊且美觀的 UML、流程圖與系統架構圖。
author: Antigravity
---

# D2 Styler 渲染指南 (d2-styler)

本技能定義了 Antigravity 如何調用 D2 CLI 工具來產出高品質的架構圖。

## 🛠️ 核心配置與安裝 (Setup)

為了確保跨電腦、跨 Session 的穩定性，本 Skill 遵循以下工具查找優先權：

1.  **系統環境變數**：優先直接呼叫 `d2` 指令。
2.  **備用絕對路徑**：若環境變數未設定，Agent 可嘗試查找範例路徑 `D:\Program Files\d2\bin\d2.exe`。

### 多電腦安裝指引 (Multi-machine Setup)

若在新電腦上使用，請依個人硬碟狀況選擇安裝路徑：

1.  **下載 D2**：從 [D2 GitHub Releases](https://github.com/terrastruct/d2/releases) 下載對應平台的執行檔。
2.  **放置位置**：建議放置於非 C 槽目錄（如 `D:\Tools\d2` 或 `D:\Program Files\d2`）。
3.  **設定環境變數 (關鍵)**：將 D2 的 `bin` 目錄路徑加入系統的 `PATH` 中。
    *   *驗證方式*：在終端機輸入 `d2 --version` 若能正確顯示版本即代表安裝成功。

## 📂 標準化專案目錄結構

Agent 在任何專案中使用此技能時，必須遵循以下結構：

```
<專案根目錄>/
├── d2_UML/
│   ├── input/      # 存放 .d2 原始碼 (不追蹤)
│   └── output/     # 存放 .svg 渲染結果 (不追蹤)
```

> [!IMPORTANT]
> `d2_UML/` 及其內容**嚴禁提交至 Git**。請確保 `.gitignore` 已包含 `d2_UML/`。

## 🏷️ 命名規則 (Naming Convention)

檔案必須採用 `{前綴}_{流水編號}_{描述}.d2` 格式：

*   `flow_` (流程圖)：範例 `flow_001_資源排程.d2`
*   `arch_` (架構圖)：範例 `arch_001_微服務拓撲.d2`
*   `seq_` (序列圖)：範例 `seq_001_API呼叫流程.d2`
*   `er_` (ER 圖)：範例 `er_001_資料庫模型.d2`
*   `class_` (類別圖)：範例 `class_001_介面定義.d2`

## ⌨️ 常用指令範例

### 1. 標準渲染 (推薦 ELK 佈局)
```powershell
d2 --layout=elk d2_UML/input/flow_001_test.d2 d2_UML/output/flow_001_test.svg
```

### 2. 即時預覽模式 (Watch)
```powershell
d2 --watch d2_UML/input/flow_001_test.d2
```

### 3. 手繪風格 (Sketch)
```powershell
d2 --sketch d2_UML/input/flow_001_test.d2 d2_UML/output/flow_001_sketch.svg
```

## 📝 D2 語法速查

### 節點與形狀 (Shapes)
*   預設矩形：`node_id: 標籤內容`
*   菱形：`node_id: 標籤 {shape: diamond}`
*   橢圓：`node_id: 標籤 {shape: oval}`
*   套件/容器：`container_id: 標籤 {shape: package}`

### 連線 (Connections)
*   單向：`a -> b`
*   雙向：`a <-> b`
*   附標籤：`a -> b: 訊息內容`

### 樣式 (Styles)
*   虛線：`style.stroke-dash: 5`
*   背景色：`style.fill: "#f5f5f5"`

## ⚖️ 安全治理政策
1.  **路徑限制**：僅限在專案內的 `d2_UML/` 或臨時的 `scratch/` 目錄下作業。
2.  **不追蹤原則**：Agent 在建立目錄後，必須檢查並更新 `.gitignore`。
