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

## 3. 自動化實作標準 (setup.ps1)
每個 Skill 應包含一個位於 `scripts/setup.ps1` 的部署腳本，並遵循以下標準：

### 3.1 腳本行為
1. **路徑偵測**：自動獲取 Skill 原始碼的絕對路徑。
2. **衝突檢查**：檢查全域路徑是否已存在同名檔案。
   - 若已存在同名連結，則提示錯誤並停止，不強制覆蓋。
3. **錯誤處理**：使用 `Try-Catch` 結構捕獲權限錯誤 (AccessDenied) 並輸出友善提示。
4. **狀態回報**：成功建立後應輸出連結的詳細資訊。

### 3.2 程式碼模板 (PowerShell)
```powershell
$SkillName = "..." # 定義 Skill 名稱
$GlobalSkillsDir = "C:\Users\kissi\.gemini\antigravity\skills"
$TargetLink = Join-Path $GlobalSkillsDir $SkillName
$SourcePath = Resolve-Path ".." # 假設腳本在 scripts 子目錄

try {
    if (Test-Path $TargetLink) {
        Write-Error "錯誤：全域路徑已存在 '$SkillName'。請先手動解除或確認是否重複。"
    } else {
        New-Item -ItemType SymbolicLink -Path $TargetLink -Target $SourcePath
        Write-Host "成功：已建立符號連結 -> $TargetLink" -ForegroundColor Green
    }
} catch {
    Write-Error "建立失敗：請檢查是否具備系統管理員權限。`n錯誤訊息：$($_.Exception.Message)"
}
```

## 4. 管理與維護 (README)
所有遵循此協議的 Skill 必須在專案 `README.md` 中進行註冊說明，並引導使用者如何執行自動化部署。
