---
name: github_cli_skill
description: 整合 GitHub CLI (gh) 工具，提供專案閱讀、Issue/PR 追蹤與 API 檢索能力。
author: Antigravity
---

# GitHub CLI Skill (github_cli_skill)

本 Skill 定義了 Antigravity 如何調用 `gh` 命令行工具來協助使用者閱讀與討論 GitHub 上的開源項目。

## 核心配置

### 工具路徑 (Executable Path)
為了確保跨 Session 的穩定性，本 Skill 優先使用以下路徑查找：
1.  系統環境變數中的 `gh`
2.  絕對路徑：`C:\Program Files\GitHub CLI\gh.exe`

### 安全治理政策 (Governance Policy)
> [!CAUTION]
> **嚴禁破壞性操作**：本 Skill 禁止執行任何涉及「刪除 (Delete)」、「修改權限 (Admin)」或「更改可見性 (Visibility)」的操作。任何產出 PR 或 Issue 的操作必須在使用者明確指令下執行。

## 常用指令範例

### 專案概覽 (Repo Overview)
用於快速瞭解一個開源專案：
```powershell
# 基本信息與 README
gh repo view <owner>/<repo>
```

### 討論追蹤 (Discussion Tracking)
用於暸解目前的開發動態：
```powershell
# 列出最近 10 個 Issue
gh issue list -R <owner>/<repo> -L 10

# 閱讀特定 Issue 的內容與留言
gh issue view <issue_number> -R <owner>/<repo> --comments
```

### 變更審閱 (Change Review)
用於討論具體的代碼實作：
```powershell
# 閱讀 PR 摘要與討論
gh pr view <pr_number> -R <owner>/<repo> --comments

# 查看 PR 的代碼差異摘要
gh pr diff <pr_number> -R <owner>/<repo>
```

## 進階應用：GitHub API
當標準指令不足時，可使用 GraphQL 調取數據：
```powershell
gh api graphql -f query='query { repository(owner:"cli", name:"cli") { stargazerCount } }'
```
