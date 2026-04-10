# 測試計畫：Antigravity 全域說明 Skill

## 1. 靜態檢修 (Static Check)
- **結構驗證**：確保 `SKILL.md` 的 YAML 前綴正確，且 `docs/` 下的所有連結路徑在本地端可用。
- **內容驗證**：確保所有官方章節內容皆已翻譯為繁體中文，且語意正確無誤。

## 2. 功能測試 (Functional Testing)
- **Symlink 連結測試**：
    - 指令：`ls C:\Users\kissi\..antigravity\skills\antigravity-manual`
    - 預期結果：顯示實體目錄 `d:\AI_Project\gemini_project\AI_Study\Antigravity\src\antigravity-manual-skill\` 的內容。
- **Skill 調度測試**：
    - 在新對話中輸入：「Antigravity 的沙箱權限有哪些等級？」
    - 預期動作：AI 使用 `view_file` 打開 `antigravity-manual/SKILL.md`，隨後根據引導打開 `docs/03-permissions-security.md`。

## 3. 回歸與錯誤處理記錄
| 測試項目 | 測試日期 | 結果 | 錯誤原因 | 修復方案 |
| :--- | :--- | :--- | :--- | :--- |
| 目錄結構初始化 | 2026/04/10 | 通過 | - | - |
| Symlink 建立 | 2026/04/10 | 通過 | - | 使用者手動執行管理員指令成功 |
| 全域規則套用 | 2026/04/10 | 通過 | - | - |
| 跨對話文件讀取 | 2026/04/10 | 通過 | - | 已由使用者新視窗驗證成功 |
