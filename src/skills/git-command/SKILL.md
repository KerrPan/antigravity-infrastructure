---
name: git-command
description: Git 操作規範與 Commit 格式指引。包含 Conventional Commits 類型定義、繁體中文撰寫準則與最佳實踐。
---

# Git 操作規範 (git-command)

本技能定義了 Antigravity 專案中所有的 Git 操作標準，旨在確保修訂紀錄的可讀性（Human-readable）與自動化處理能力（Machine-readable）。

## 🌐 語言規範 (Language Policy)

> [!IMPORTANT]
> **全數使用繁體中文**：所有的 Commit 標題（Subject）與正文（Body）內容，除技術專有名詞外，必須統一使用繁體中文撰寫。

---

## 📝 Commit 格式：Conventional Commits

Commit 訊息應遵循以下結構：
```text
<類型>(作用域): <描述>

[正文]

[頁腳]
```

### 常見類型 (Types)
- **`feat`**: 新增功能（New Feature）。
- **`fix`**: 修補錯誤（Bug Fix）。
- **`docs`**: 僅變更說明文件（Documentation）。
- **`style`**: 不影響程式邏輯的代碼格式更動（如空白、格式化、分號）。
- **`refactor`**: 代碼重構。既不是修復 Bug 也不是新增功能的改動。
- **`perf`**: 提升效能的代碼變更。
- **`test`**: 新增或修正測試案例。
- **`chore`**: 輔助工具、依賴管理或建置程序的變更（如更新 `.gitignore`）。

---

## 📏 撰寫七大原則 (The Seven Rules)

1.  **區隔標題與正文**：兩者之間必須留一行空白。
2.  **標題限制 50 個字元**：簡明扼要。
3.  **標題不加句點**：結尾不需要 `.`。
4.  **使用祈使句**：例如 `新增股票爬蟲功能` 而非 `已新增了股票爬蟲功能`。
5.  **正文每行限制 72 個字元**：確保在不同終端機能正確呈現。
6.  **說明「為什麼」與「做了什麼」**：而非描述「如何做」。
7.  **確保原子性 (Atomic Commits)**：一次 Commit 只處理一個邏輯變更。

---

## 💡 範例 (Examples)

### 正確範例
```text
feat(stock): 新增個股基本面抓取功能

- 串接 Yahoo Finance API 獲取營收數據
- 新增 DataParser 模組處理 JSON 轉換
- 修正原本資料格式不統一的問題
```

### 錯誤範例
```text
fixed some bugs.
```

## 🛠️ 操作準則

*   **Commit 前檢查**：在執行 `git commit` 前，必須檢查暫存區 (Staging Area) 的內容是否與 Commit 訊息描述完全一致。
*   **版本控制誠信**：嚴禁在一次 Commit 中混雜多種不相關的變更。若有多個任務，請拆分為多次 Commit。
