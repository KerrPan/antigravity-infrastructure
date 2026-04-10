# 技術規格書：全域 Skill 管理協議 (Skill Management Protocol)

## 1. 目標
建立一套標準化的程序，將專案內開發的 Skill 安全且自動化地掛載至 Antigravity 的全域路徑，並確保跨環境的一致性。

## 2. 核心規範
### 2.1 命名慣例 (Naming Convention)
- **原始碼路徑**：必須位於 `src/<SKILL_NAME>/`。
- **全域掛載路徑**：`C:\Users\kissi\.gemini\antigravity\skills\<SKILL_NAME>`。
- **一致性**：全域路徑下的捷徑名稱必須與 `src/` 下的原始目錄名稱完全一致。

### 2.2 部署機制
- **連結類型**：強制使用 **Symbolic Link (符號連結)**。
- **優點**：即時同步檔案變更，不需手動複製。
- **限制**：Windows 環境下通常需要 **系統管理員權限** 才能建立符號連結。

## 3. 部署交付標準 (Manual Command Delivery)
為了維持環境純淨並避免權限自動化帶來的複雜性，本專案不建立部署腳本。取而代之的是，AI 在完成新 Skill 開發時，必須根據以下標準主動提供布署指令：

### 3.1 指令格式標準
1. **工具選用**：固定提供 PowerShell 的 `New-Item` 指令。
2. **絕對路徑**：AI 必須根據當前環境（如 `D:\AI_Project\...`）提供完整的絕對路徑。
3. **強制參數**：必須包含 `-ItemType SymbolicLink`。

### 3.2 交付模板
AI 應在任務總結時提供類似以下的程式碼區塊：

```powershell
# 請以系統管理員權限執行以下指令
New-Item -ItemType SymbolicLink -Path "C:\Users\kissi\.gemini\antigravity\skills\<SKILL_NAME>" -Target "<YOUR_PROJECT_PATH>\src\<SKILL_NAME>"
```

### 3.3 錯誤排除指引
交付指令時需同步附帶以下提醒：
- **權限要求**：必須使用「系統管理員 (Administrator)」身分執行。
- **衝突處理**：若目標連結已存在，請先手動刪除 (rm) 後再重新執行。

## 4. 管理與維護 (README)
所有遵循此協議的 Skill 必須在專案 `README.md` 中進行註冊說明，並引導使用者如何執行自動化部署。
