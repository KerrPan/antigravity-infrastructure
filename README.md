# Antigravity 全域設定管理中心

本專案致力於集中管理 Antigravity 的全域配置、說明文件與自定義技能 (Skills)。透過將全域設定「專案化」，我們得以實現版本控制、結構化編寫，並確保 AI 在本機環境下擁有一致且精確的行為基準。

## 🧠 核心機制
- **循環推理與 ACT (Looped Reasoning)**：借鑒 OpenMythos 架構，對於複雜計畫生成導入「自我批判-修正」循環。
- **動態分解 (Spawning)**：當任務風險較高時，自動啟動「嚴格型」批判者子代理進行紅隊演練。
- **回饋飛輪 (Flywheel)**：即時捕捉使用者修正，並記錄推理深度 (Loops) 與自評得分 (Score)。

## 📂 目錄結構
- `.gemini/`：存放專案特定的 AI 狀態與設定。
- `docs/specs/`：存放全域功能或 Skill 的技術規格書 (Specs)與測試計畫。
- `docs/ADR/`：存放架構決策紀錄 (Architecture Decision Records)。
- `src/skills/`：存放實際的 Skill 原始碼（例如：`antigravity-manual`、`github-cli`）。
- `tests/`：存放驗證指令或測試腳本。

## 🛠️ 全域 Skill 處理方式 (SOP)

為了讓全域 AI 此隨時能取用本專案開發的技能，請遵循以下維護標準：

### 1. 建立與編寫
*   **命名規範**：技能目錄與 `SKILL.md` 中的 `name` 必須統一使用 **kebab-case (`-`)**（例如 `my-new-skill`），嚴禁使用底線或混用大小寫。
*   **Skill 存放路徑**：每個技能必須在 `src/skills/` 下擁有獨立資料夾，且內部必須包含 `SKILL.md`。
*   **YAML 標頭**：`SKILL.md` 頂部必須定義 `name` 與 `description`，這是 AI 判斷是否調用的關鍵。
*   **分支文件**：若主題龐大（如官方手冊），應將內容拆分為獨立的 Markdown 檔案並由 `SKILL.md` 指引，以優化 Token 消耗。

### 2. 部署 (全域掛載)
為了確保跨環境的一致性，本專案採用 **手動符號連結 (Symbolic Link)** 進行掛載。

#### 部署 SOP
1.  **獲取指令**：在開發完成後，AI 會根據 [全域 Skill 管理協議](file:///d:/AI_Project/gemini_project/AI_Study/Antigravity/docs/specs/skill_management_protocol.md) 提供對應的 PowerShell 指令。
2.  **執行掛載**：
    *   以 **系統管理員** 權限開啟 PowerShell。
    *   複製並執行 AI 提供的 `New-Item` 指令。
3.  **衝突處理**：若目標路徑已存在舊連結，請先執行 `rm <Target_Path>` 刪除後再重試。

#### 指令範本 (PowerShell)
```powershell
New-Item -ItemType SymbolicLink -Path "C:\Users\kissi\.gemini\antigravity\skills\<SKILL_NAME>" -Target "<PROJECT_PATH>\src\skills\<SKILL_FOLDER>"
```

### 3. 指引與授權
*   **更新全域規則**：修改 `C:\Users\kissi\.gemini\GEMINI.md`，在 `## 全域資源參考` 區塊加入新 Skill 的描述，告知 AI 在何種任務下應優先調用該技能。
*   **權限管理**：若 Skill 包含腳本或工具，請確保在全域或專案規則中明確宣告其動作白名單 (Whitelist)。

## 🔄 更新流程
1.  在本專案修改 Markdown 或配置。
2.  由於使用 Symlink，系統端會即時同步，不需重新安裝。
3.  測試變更是否符合預期。
4.  Commit 並 Push 變更至 Git（建議）。

## ⚙️ 必要環境 (Prerequisites)
- **Node.js**: v20.0.0+ (用於執行 OpenCLI)
- **OpenCLI**: `npm install -g @jackwener/opencli`
- **Browser Bridge**: 需在 Chrome 載入 [OpenCLI 擴充功能](https://github.com/jackwener/OpenCLI/releases)

---
*Last Updated: 2026-04-10 (Refactored Structure)*
