---
name: opencli
description: 高效網頁內容擷取技能。利用 OpenCLI 工具實現數據化讀取，繞過視覺互動，支援 GitHub 等 80+ 網站。
---

# OpenCLI 高效網頁讀取指南

本技能整合了 [OpenCLI](https://github.com/jackwener/OpenCLI) 工具，為 Antigravity 提供高效、數據化的網頁內容擷取能力。

> [!TIP]
> **官方參考連結 (Official Source)**: [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI)

## 🛠️ 核心工具說明 (Tool Directory)

當您需要讀取網頁內容或診斷環境時，請使用以下工具指令：

1.  **環境診斷 (`opencli_doctor`)**
    *   內容：執行 `opencli doctor` 以檢查背景服務 (Daemon) 與瀏覽器擴充功能之連線狀態。
2.  **高效網頁讀取 (`opencli_web_read`)**
    *   內容：執行 `opencli web read --url <URL>`。
    -   優點：將網址（特別是 GitHub 頁面）直接轉換為 Markdown 格式，不開啟可見視窗，自動處理 JavaScript 渲染。

## 📖 調用準則 (Usage Guidelines)

*   **優先性能**：對於 README、技術文件或新聞等「文字為主」的網頁，請優先使用本技能，嚴禁在這些場景下使用 `browser_subagent` 進行慢速的視覺模擬（滾動/截圖）。
*   **環境依賴**：執行前請確保 Chrome/Edge 已開啟且載入了 `OpenCLI Browser Bridge` 擴充功能。
*   **暫存清理**：使用 `opencli web read` 等指令後，必須主動檢查並清理工作區中自動產生的暫存資料夾（如 `web-articles`），以維持環境整潔。
*   **錯誤重試**：若回傳「Extension not connected」，請提示使用者檢查瀏覽器是否開啟。
*   **繁體中文輸出**：接收到網頁內容後，請根據內容進行摘要或分析，並始終以繁體中文回應使用者。
