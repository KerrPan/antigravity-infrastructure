# Antigravity 全域設定管理中心

本專案致力於集中管理 Antigravity 的全域配置、說明文件與自定義技能 (Skills)。透過將全域設定「專案化」，我們得以實現版本控制、結構化編寫，並確保 AI 在本機環境下擁有一致且精確的行為基準。

## 📂 目錄結構
- `.gemini/`：存放專案特定的 AI 狀態與設定。
- `docs/specs/`：存放全域功能或 Skill 的技術規格書與測試計畫。
- `src/`：存放實際的 Skill 原始碼（例如：`antigravity-manual-skill`）。
- `tests/`：存放驗證指令或測試腳本。

## 🛠️ 全域 Skill 處理方式 (SOP)

為了讓全域 AI 此隨時能取用本專案開發的技能，請遵循以下維護標準：

### 1. 建立與編寫
*   **Skill 根目錄**：每個技能必須在 `src/` 下擁有獨立資料夾，且內部必須包含 `SKILL.md`。
*   **YAML 前言**：`SKILL.md` 頂部必須定義 `name` 與 `description`，這是 AI 判斷是否調用的關鍵。
*   **分支文件**：若主題龐大（如官方手冊），應將內容拆分為獨立的 Markdown 檔案並由 `SKILL.md` 指引，以優化 Token 消耗。

### 2. 部署 (全域掛載)
為了確保跨環境的一致性，本專案採用 **手動符號連結 (Symbolic Link)** 進行掛載。

#### 部署 SOP
1.  **獲取指令**：在開發完成後，AI 會根據 [全域 Skill 管理協議](file:///d:/AI_Project/gemini_project/AI_Study/Antigravity/docs/specs/skill_management_protocol.md) 提供對應的 PowerShell 指令。
2.  **執行掛載**：
    *   以 **系統管理員** 權限開啟 PowerShell。
    *   複製並執行 AI 提供的 `New-Item` 指令。
3.  **衝突處理**：若目標路徑已存在舊連結，請先執行 `rm <Target_Path>` 刪除後再重試。

#### 指令範本
```powershell
New-Item -ItemType SymbolicLink -Path "C:\Users\kissi\.gemini\antigravity\skills\<SKILL_NAME>" -Target "<PROJECT_PATH>\src\<SKILL_FOLDER>"
```

### 3. 指引與授權
*   **更新全域規則**：修改 `C:\Users\kissi\.gemini\GEMINI.md`，在 `## 全域資源參考` 區塊加入新 Skill 的描述，告知 AI 在何種任務下應優先調用該技能。
*   **權限管理**：若 Skill 包含腳本或工具，請確保在全域或專案規則中明確宣告其動作白名單 (Whitelist)。

## 🔄 更新流程
1.  在本專案修改 Markdown 或配置。
2.  由於使用 Symlink，系統端會即時同步，不需重新安裝。
3.  測試變更是否符合預期。
4.  Commit 並 Push 變更至 Git（建議）。

---
*Last Updated: 2026-04-10*
