# 技術規格書：OpenCLI 整合能力提升計畫

## 1. 背景與動機
在先前的任務（如 `antigravity-manual-skill` 製作）中，本 AI 代理在讀取說明文件網頁時，必須啟動瀏覽器並進行人工式的滾動、點擊與截圖。這種「模擬真人操作」的方式對於以文字為主的內容擷取效率極低，且容易受頁面加載速度與互動機制干擾。

本計畫旨在整合 [OpenCLI](https://github.com/jackwener/OpenCLI) 工具，將網頁內容擷取從「視覺模擬互動」提升為「指令化/數據化擷取」，以達到高效、穩定的開發輔助能力。

## 2. 核心目標
1.  **指令化擷取**：透過 OpenCLI 提供的 CLI 介面，直接獲取網頁的 Markdown 或 JSON 資料。
2.  **Session 復用**：重用使用者瀏覽器已登入的 Session，解決需要權限才能訪問的網頁讀取問題。
3.  **Skill 化封裝**：將 OpenCLI 的功能封裝為 Antigravity 的原生 Skill，讓 AI 代理能像調用檔案系統一樣調用網頁數據。

## 3. 技術方案
### 3.1 元件構成
-   **OpenCLI Core**：基於 Node.js 的全域工具（`@jackwener/opencli`）。
-   **Browser Bridge Extension**：安裝於使用者瀏覽器的插件，提供 CDP 控制能力。
-   **OpenCLI Skill**：自定義的 Antigravity Skill，包含 `opencli_read` 與 `opencli_browser_control` 等具體工具。

### 3.2 運作流程
1.  AI 接收到讀取網址的請求。
2.  AI 調用 `opencli_skill` 中的工具。
3.  工具執行 `opencli browser get --url <target> --format md` 指令。
4.  OpenCLI 透過 Bridge Extension 從後台瀏覽器直接提取並清理 DOM 內容。
5.  AI 取得乾淨的 Markdown 內容，跳過所有視覺互動與截圖步驟。

## 4. 交付物清單
-   `docs/specs/opencli_integration_spec.md` (本文件)
-   `src/skills/opencli_skill/`：整合後的 Skill 原始碼。
-   `docs/adr/001_opencli_adoption.md`：架構決策紀錄。

## 5. 待確認事項 (Ambiguity Elimination)
> [!IMPORTANT]
> 在開始開發前，請確認以下資訊：
> 1.  **安裝授權**：是否允許我在專案或系統中安裝 `@jackwener/opencli`？
> 2.  **環境確認**：你是否已在 Chrome/Edge 中手動安裝了 [OpenCLI Browser Bridge](https://github.com/jackwener/opencli/releases) 擴充功能？（這部分 AI 無法代勞）
> 3.  **預期場景**：除了純文字說明網頁外，是否有其他特定網站（例如：需要登入的 GitHub 頁面、Wiki 系統）是你優先希望測試的？
