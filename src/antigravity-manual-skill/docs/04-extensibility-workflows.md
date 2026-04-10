# 擴充功能 (Extensibility: Rules, Workflows, Skills)

Antigravity 提供多種方式讓使用者定義自己的 AI 行為軌跡與知識庫。

## 1. 規則 (Rules)
規則是直接影響 AI 決策路徑的指令。
*   **全域規則**：定義於 `~/.gemini/GEMINI.md`，影響所有對話。
*   **專案規則**：存放於工作區的 `.agents/rules/` 目錄中。
*   **特性**：Markdown 格式，單一文件建議不超過 12,000 個字元。AI 會在對話開始前自動加載這些上下文。

## 2. 工作流 (Workflows)
工作流是一系列預定義的步驟，用於標準化複雜任務。
*   **定義**：以 Markdown 文件定義流程與每個步驟的預期。
*   **觸發方式**：在對話框輸入 `/` 即可喚出選單，或輸入 `/工作流名稱` 直接觸發。

## 3. 技能 (Skills)
技能是功能最強大的擴充方式，可提供額外的工具、腳本或專屬知識。
*   **標準**：符合 `agentskills.io` 開放標準。
*   **結構**：必須包含一個資料夾與 `SKILL.md` 索引文件。其內可包含 `scripts/`, `docs/`, `examples/` 等子目錄。
*   **索引定義**：`SKILL.md` 頂部必須包含 YAML 前言 (Frontmatter)，範例如下：
    ```yaml
    ---
    name: my-custom-skill
    description: 描述這個技能的作用，幫助 AI 判斷何時調用。
    ---
    ```
*   **路徑**：全域位於 `~/.gemini/antigravity/skills/`；本機位於工作區的 `.agents/skills/` 或隱藏目錄。
