---
name: anti-planner
description: Antigravity 全域開發規劃師。基於 Archon 的防呆驗證與 Spec-kit 的規格驅動 (SDD) 哲學，強制 AI 在執行前產出標準化且具備邊界防護的 implementation_plan。
---

# Anti-Planner 技能 (全域開發規劃師)

歡迎調用 `anti-planner`。本技能深度融合了 GitHub **[Spec-Kit] (規格驅動與模組化憲法)** 以及 **[Archon] (執行防呆與邊界隔離)** 兩大開源專案的核心哲學。

> [!CAUTION]
> **觸發時機**：當您（AI）接到任何系統開發或邏輯修改的任務，並準備撰寫 `implementation_plan.md` 時。
> **核心禁令**：在沒有產出符合本規範的 `implementation_plan.md`，並取得人類開發者的同意前，**絕對禁止修改或生成任何業務代碼**。

---

## 🎯 核心準則與強制覆寫

當您進入規劃模式 (Planning Mode) 時，您必須將以下 5 大護欄，強制寫入您的 `implementation_plan.md` 中：

### 1. 資源盤點與代碼庫為王 (Primitives Inventory)
您**不能憑空捏造**開發方案。
*   **動作**：在規劃前，必須使用 `grep_search` 或 `view_file` 調查專案。
*   **輸出**：計畫中必須包含清單，列出「既有資源」（有哪些已存在的資料結構、API、錯誤處理機制可以重複使用）。

### 2. 規格驅動的資料與狀態架構 (Spec-Driven State)
在撰寫任何實作細節前，必須先釐清系統「如何互動」。
*   **輸出**：計畫中必須以 ASCII 圖或具體條列方式，描繪出 `Before State (修改前)` 與 `After State (修改後)` 的 UX 互動與資料流向 (Data Flow)。

### 3. 重中之重：防護網邊界 (NOT Building)
所有計畫都必須防止範圍蔓延 (Scope Creep)。
*   **輸出**：您必須設立專屬章節 `## NOT Building (不做的範圍)`。精準寫出哪些延伸功能「不包含在本次任務內」，確保單一職責與環境可控性。

### 4. 驗證哨站 (Command Validation)
AI 不該產出無法驗證的代碼。
*   **輸出**：計畫書中的每一個「開發步驟」，都必須綁定一行具體的 **「驗證指令」**（例如：`npm run lint`、`go test './...'` 或確保畫面無 js 報錯）。只有前一個步驟驗證通過，AI 才能執行下一個步驟。

### 5. 文件即程式碼 (Docs as Code)
代碼變更與文件更新必須綁定在同一個任務週期。
*   **動作**：如果邏輯或介面有變，必須同步盤點並更新註解、型別定義、README 或建立 ADR (Architecture Decision Records - 架構決策紀錄)。
*   **輸出**：計畫中必須規劃專屬的「文件更新步驟」，確保持續維護活文件 (Living Documentation)。

---

## 📝 標準化 implementation_plan.md 範本

未來的 `implementation_plan.md` 必須嚴格比照下方結構撰寫：

```markdown
# [專案/模組名稱] 實作計畫

## 1. 既有資源盤點 (Primitives Inventory)
*   **[模組 A]**: (檔案路徑:行數) - (說明為何要複用此模組的命名格式或邏輯)
*   **[模組 B]**: (檔案路徑:行數) - (既有的資料結構，將以此為標準擴充)

## 2. 規格與資料流架構 (Spec-Driven Architecture)
### 2.1 狀態轉換圖 (Before/After)
[Before State]
User -> (舊介面) -> 缺少資料

[After State]
User -> (新介面) -> [資料整理器] -> 統一格式輸出

## 3. 防護網界線 (NOT Building)
> [!WARNING]
> 本任務**絕對不會**包含以下實作：
> - 1. [超出的功能 A]
> - 2. [不相關的模組 B 修改]

## 4. 實作步驟與驗證哨站 (Tasks & Validation)
* [ ] **Step 1: [具體實作任務描述]**
  - 使用模組: [引用資源盤點中的模組]
  - **Validation Command**: `[必須放入可執行的檢驗指令，例如 npm test 或特定腳本]`
* [ ] **Step 2: [下一步...]**
  - **Validation Command**: `[...]`

## 5. 文件更新計畫 (Docs as Code)
*   [列出本次任務需同步更新的文件，例如 README、註解、新增 ADR 等]

## 6. 待人類決策 (Open Questions)
*   [列出需要人類架構師提早決定的介面或邏輯分歧點]
```

## 執行流程
1. 立即停止任何不必要的代碼撰寫。
2. 開始對專案進行探索 (Explore)，收集基礎資源要素。
3. 輸出完美符合上述格式的 `implementation_plan.md`。
4. 等待人類批准。
