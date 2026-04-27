---
name: anti-planner
description: Antigravity 全域開發規劃師。基於 Archon 的防呆驗證與 Spec-kit 的規格驅動 (SDD) 哲學，具備動態分解 (T2) 與基礎設施自動初始化能力。
---

# Anti-Planner 技能 (全域開發規劃師)

歡迎調用 `anti-planner`。本技能深度融合了 GitHub **[Spec-Kit] (規格驅動與模組化憲法)** 以及 **[Archon] (執行防呆與邊界隔離)** 核心哲學，並具備「全域感知」與「基礎設施部署」能力。

> [!CAUTION]
> **觸發時機**：當您（AI）接到任何系統開發或邏輯修改的任務，並準備撰寫 `implementation_plan.md` 時。
> **核心禁令**：在沒有產出符合本規範的 `implementation_plan.md`，並取得人類開發者的同意前，**絕對禁止修改或生成任何業務代碼**。

---

## 🎯 核心準則與強制覆寫

當您進入規劃模式 (Planning Mode) 時，您必須將以下 7 大護欄，強制寫入您的 `implementation_plan.md` 中：

### 0. 專案基礎設施檢查 (Infrastructure Guard)
AI 進入任何專案時，必須確保根目錄具備代理憲法 (`AGENTS.md`) 與回饋飛輪 (`FLYWHEEL.md`)。
*   **動作**：若缺失，必須在實作計畫的 Step 0 提議使用「嵌入式模板」進行初始化部署，並更新 `.gitignore`。

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
代碼變更與文件更新必須綁定在同一個任務週期。 **嚴禁使用籠統描述**。
*   **動作**：如果邏輯或介面有變，必須同步盤點並更新**註解、型別定義、README** 或產出/更新相關規格文檔。
*   **文檔準則**：
    *   **API/功能異動**：使用 `SPEC.md.template` 產出/更新 `docs/specs/SPEC-xxx.md`。
    *   **重大架構決策**：使用 `ADR.md.template` 產出/更新 `docs/ADR/ADR-xxx.md`。
*   **輸出**：計畫中必須規劃具體的「文件更新步驟」，並標明「路徑 + 行號區段/章節名」。

### 6. 動態分解與子代理驗證 (Dynamic Decomposition)
AI 不應在單一 Context 下完成所有高風險決策。
*   **動作**：若任務涉及核心商業邏輯、複雜安全模組或外部市場分析，應規劃「Spawn Sub-agent」進行側向交叉檢驗。同時，若使用者在執行中提供「糾正信號」，必須即時調整計畫圖。

### 7. 自適應循環推理 (Adaptive Looped Reasoning)
遵循 `AGENTS.md` 中的循環協議，提升計畫穩健性。
*   **動作**：對於 Level 2 任務，在提交 `implementation_plan.md` 前，必須啟動一名「嚴格挑刺型」Critic Sub-agent。
*   **輸出要求**：最終計畫中不顯示審核過程紀錄，僅呈現經由「批判-修正」循環後的最優結果。

### 8. 變更聯動與文件溯源 (Change Linkage & Traceability)
防止內化知識導致的規則遺失與模板脫鉤。
*   **動作**：修改任何專案標準文件（如 `AGENTS.md`, `FLYWHEEL.md`）時，必須同步檢查其在 `src/skills/anti-planner/templates/` 下的對應模板。
*   **準則**：所有 Agent 的行為邏輯變更，必須在代碼庫中具備對應的文件說明（如 `AGENTS.md` 或 `SKILL.md`），嚴禁僅依賴內化知識執行。

---

## 📝 標準化 implementation_plan.md 範本

未來的 `implementation_plan.md` 必須嚴格比照下方結構撰寫：

```markdown
# [專案/模組名稱] 實作計畫

## 0. 基礎設施部署 (Infrastructure Init) - *若已存在則略過*
* [ ] **Initialize AGENTS.md & FLYWHEEL.md**
  - 使用來自 `anti-planner` 技能的嵌入式模板。
* [ ] **Update .gitignore**
  - 建議忽略 `implementation_plan.md`, `task.md`, `walkthrough.md` 等臨時執行文件。

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
  - **Validation Command**: `[必須放入可執行的檢驗指令]`
* [ ] **Step 2 (Dynamic Verification): Spawn Sub-agent**
  - 任務內容：[描述子代理任務，例如進行獨立的安全 Review]
  - **Validation Command**: `[比較子代理結果與主計畫的 diff]`

## 5. 文件更新計畫 (Docs as Code)
> [!IMPORTANT]
> 嚴禁使用籠統描述（如「更新 README」）。必須為具體「路徑 + 行號區段/章節名」。
*   [ ] **README.md**: [章節名稱] - 同步修改 [具體功能/API/配置] 定義。
*   [ ] **docs/specs/**: [NEW/MODIFY] [SPEC-xxx-名稱.md] - 依據 `SPEC.md.template` 更新規格真相。
*   [ ] **docs/ADR/**: [NEW/MODIFY] [ADR-xxx-名稱.md] - 依據 `ADR.md.template` 紀錄核心架構決策。
*   [ ] 其他受影響文件。

## 待人類決策 (Open Questions)
*   [列出需要人類架構師提早決定的介面或邏輯分歧點]
```

## 📝 標準化 task.md 範本

請在 `task.md` 模板的最末端，固定加入以下「原子任務」：

```markdown
- [ ] **[MANDATORY] 完工一致性自檢 (Sync Audit)**
  - [ ] 主動讀取本次修改的「代碼實作」與「對應文檔」。
  - [ ] 確認 ADR 與 README 中的描述是否與最終代碼邏輯 100% 吻合（例如參數名、請求方法、決策路徑）。
  - [ ] 若有不符，必須在此步驟立即修正文檔，禁止帶傷完工。
```

---

## 🧬 嵌入式基礎設施模板 (Embedded Templates)

> [!TIP]
> **Source of Truth**: AI 應優先嘗試讀取技能目錄下的 `./templates/*.template` 檔案。若無法讀取，則使用以下嵌入式備援。

### [Template: AGENTS.md]
```markdown
# Antigravity Agentic Manifesto (代理人行為憲法)
本專案遵循「On the Loop」協作模式。
1. Humans steer. Agents execute.
2. 任何重大決策需通過 AGENTS.md 定義之 T2 驗證。
3. 遵循 §5 循環推理與 ACT 停機協議：Think deep, Halt smart.
### 常用指令 (Common Commands)
- **List Skills**: `ls src/skills/`
- **Check Flywheel**: `cat FLYWHEEL.md`
```

### [Template: FLYWHEEL.md]
```markdown
# Antigravity Feedback Flywheel (回饋飛輪紀錄)
| 日期 | 場景 (Scenario) | 使用者修正 (Judgment Signal) | 潛在規則 | 狀態 |
| :--- | :--- | :--- | :--- | :--- |
```

---

## 執行流程
1. 立即停止任何代碼撰寫，掃描當前工作區根目錄偵測基礎設施狀態。
2. 開始對專案進行探索 (Explore)，收集基礎資源要素。
3. 輸出完美符合上述格式的 `implementation_plan.md`。
4. 等待人類批准。
