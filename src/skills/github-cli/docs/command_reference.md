# GitHub CLI 指令參考手冊 (Command Reference)

本文件詳述了在 Antigravity 環境中常用的 `gh` 指令用法，主要針對「讀取與討論」場景進行優化。

## 1. Repository (倉庫操作)

### 檢視倉庫
```powershell
gh repo view <owner>/<repo> [--web]
```
-   預設顯示 README 與 Metadata。
-   使用 `--web` 可直接在瀏覽器開啟（需使用者手動查看）。

### 搜索倉庫
```powershell
gh repo search "<keyword>" --limit 10
```

## 2. Issues (議題管理)

### 列出議題
```powershell
gh issue list -R <repo> --state open --author "<username>"
```

### 閱讀議題細節
```powershell
gh issue view <id> -R <repo> --comments
```
-   `--comments` 對於「討論」極其重要，應預設帶上。

## 3. Pull Requests (拉取請求)

### 列出 PR
```powershell
gh pr list -R <repo> --state open
```

### 查看 PR 變更詳情
```powershell
gh pr view <id> -R <repo> --comments
```

### 查看代碼差異 (Diff)
```powershell
gh pr diff <id> -R <repo>
```
-   用於深度討論代碼實裝細節。

## 4. API (進階查詢)

當標準指令無法滿足需求（例如需要抓取特定 Commit 或 Stargazer 趨勢）時使用。

### GraphQL 範例
```powershell
gh api graphql -f query='
  query($name:String!, $owner:String!) {
    repository(owner:$owner, name:$name) {
      releases(last:1) {
        nodes { tagName, publishedAt }
      }
    }
  }' -f owner="cli" -f name="cli"
```

## 5. 安全作業準則
-   **任何** `gh pr merge`, `gh repo delete`, `gh label add` 等寫入指令，若非使用者明確逐字要求，AI 不得主動發起。
-   在討論開源項目時，應以 `view` 指令為主。
