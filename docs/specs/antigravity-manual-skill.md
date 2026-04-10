# 技術規格書：Antigravity 全域說明 Skill (antigravity-manual)

## 1. 專案目標
將 Antigravity 的官方文件 (Docs) 轉化為本機可管理的 Skill，使 AI 具備隨時查閱系統規範的能力，並能根據不同主題（Agent, Tool, Permission）讀取對應的子文件以優化上下文長度。

## 2. 目錄結構與檔案清單
Skill 根目錄：`src/antigravity-manual-skill/`

- `SKILL.md`：核心入口與引導指令。
- `docs/`：子手冊存放區。
    - `01-core-concepts.md`：核心概念與術語。
    - `02-agent-configuration.md`：Agent 模式與配置。
    - `03-permissions-security.md`：沙箱、權限與隱私。
    - `04-extensibility-workflows.md`：Skill, Workflow, Rules 深度定義。
    - `05-native-tools-browsing.md`：原生工具與 Browser Subagent 指引。

## 3. 功能邏輯 (SKILL.md 邏輯)
- **索引與調度**：AI 載入 SKILL 時，會優先閱讀此檔。檔案中需明確說明各 `docs/*.md` 的內容範圍。
- **指示句式**：當 AI 偵測到使用者請求涉及「系統配置」或「規則撰寫」時，必須優先 `view_file` 並讀取對應文件，而非自行推測。

## 4. 全域部署方案
- **方法**：在 `C:\Users\kissi\.gemini\antigravity\skills\` 下建立名為 `antigravity-manual` 的 **Symbolic Link**，指向本專案的 `src/antigravity-manual-skill/`。
- **依賴**：在全域 `GEMINI.md` 中加入：
  > 關於 Antigravity 的核心配置、規則與進階用法，應優先調用並參考 `antigravity-manual` skill。

## 5. 測試與驗證
- **覆蓋驗證**：檢查所有官方文檔中的主要關鍵字 (e.g., capability, subagent, implicit memory) 是否均有對應解釋。
- **跨對話驗證**：在非本專案的 Conversation 中測試 Skill 是否能被正確識別與執行。
