---
name: markitdown
description: 多格式文檔轉換技能。能將 PDF, Word, Excel, PowerPoint 等二進位文件在本地端轉換為結構化 Markdown。
---

# Markitdown 文檔轉換指南

本技能整合了 [microsoft/markitdown](https://github.com/microsoft/markitdown) 工具，為 Antigravity 提供本地端、高效且 Token 友善的文件閱覽能力。

> [!IMPORTANT]
> **隱私與效能保障**：本技能僅在本地執行，且預設禁用雲端 OCR 與影像描述功能。這不僅保護了敏感文檔隱私，更避免了非必要的雲端 Token 支出。

## 🛠️ 核心工具說明 (Tool Directory)

當您需要讀取或轉換非純文字文檔（PDF, Office 等）時，請使用以下工具指令：

1.  **文檔轉換至 Markdown (`markitdown_convert`)**
    *   內容：執行虛擬環境中的 python 腳本進行轉換。
    *   路徑：`src/skills/markitdown/.venv/Scripts/python.exe src/skills/markitdown/converter_wrapper.py --file <絕對路徑>`
    *   特性：
        -   **自動結構化**：保留表格、標題層級與清單格式。
        -   **自動優化**：讀取時自動剔除 `NaN` 噪點，提升 AI 處理效率與節省 Token。
        -   **在地化輸出**：轉換後的 `.md` 檔案將統一存放於專案根目錄下的 `temp_md_file/` 目錄中。
        -   **檔名規則**：使用原始檔名，重複時自動覆蓋。

## 📖 調用準則 (Usage Guidelines)

*   **優先讀取 MD**：當使用者提供 PDF 或 Office 檔案路徑時，請**優先執行轉換**，並讀取產出的 `.md` 內容作為參考，嚴禁直接嘗試「猜測」二進位檔案內容。
*   **儲存管理**：所有產出的轉換結果均位於 `temp_md_file/`。若您需要讀取轉換後的內容，請在轉換成功後查看該目錄下的對應檔案。
*   **拒絕猜測**：若轉換失敗（例如損毀檔案），請如實告知使用者，不要捏造內容。
*   **規格對標**：本技能之開發遵循 `antigravity-manual` 的擴充規範與專案 `README.md` 的環境定義。

## 🧪 驗證範例 (Verification Example)

```bash
# 轉換一個 Excel 報表
d:/AI_Project/gemini_project/AI_Study/Antigravity/src/skills/markitdown/.venv/Scripts/python.exe d:/AI_Project/gemini_project/AI_Study/Antigravity/src/skills/markitdown/converter_wrapper.py --file d:/AI_Project/gemini_project/AI_Study/Antigravity/tests/sample.xlsx
```
