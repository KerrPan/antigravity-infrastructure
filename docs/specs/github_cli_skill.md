# 技術規格書：GitHub CLI 整合 Skill (github_cli_skill)

## 1. 目標
建立一個專屬的 Skill，讓 Antigravity 環境能標準化、安全地調用 GitHub CLI 工具，用以閱讀、分析與討論 GitHub 上的開源項目。

## 2. 目錄結構
src/github_cli_skill/
├── SKILL.md                 # Skill 主描述文件
└── docs/                    # 詳細命令用法與示例
    └── command_reference.md  # 常用讀取命令參考

## 3. 功能範圍
根據 `cli/cli` 官方文件，本 Skill 將聚焦於以下「唯讀與討論相關」指令：
- **Repository**: view, clone, search
- **Issues/PRs**: list, view, status
- **Discussions**: list, view (如開啟)
- **API**: 支援經由 `gh api` 進行自定義 GraphQL/REST 查詢

## 4. 安全限制與治理 (Governance)
**強烈限制**：嚴禁執行任何具有破壞性或修改權限的操作。AI 在調用此 Skill 時必須遵守以下禁斷：
- 禁止 `gh repo delete` 或任何涉及刪除倉庫的操作。
- 禁止 `gh api -X DELETE`。
- 禁止更改任何倉庫的 visibility (public/private) 或管理協作者。
- 禁止刪除 Issue 或 Pull Request。

## 5. 技術實現細節
- **路徑自檢**：調用指令時應優先檢測 `gh` 是否在 $PATH 中。若不可用，則回退至 `C:\Program Files\GitHub CLI\gh.exe`。
- **輸出解析**：指令執行結果應格式化為 Markdown 或 JSON 以利於上下文理解。
- **身分驗證**：調用前應確認 `gh auth status` 為登入狀態。
