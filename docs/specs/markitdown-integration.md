# 規格書：microsoft/markitdown 技能整合 (markitdown-integration)

## 1. 目的與背景
本規格書定義如何將 `microsoft/markitdown` 工具整合至 **Antigravity** 框架中，作為一個獨立的技能 (Skill)。
目標是提供 AI 代理在本地端將二進位文件（PDF, Word, Excel, PPT 等）轉換為結構化 Markdown 的能力，以提升 Token 使用效率並維持輸出的結構化資訊。

## 2. 需求場景 (User Scenarios)
- **場景 A**: 使用者提供一個產品規格文檔 (docx)，要求 AI 根據內容撰寫測試腳本。
- **場景 B**: 使用者提供一個數據報表 (xlsx)，要求 AI 進行數據分析。
- **場景 C**: AI 在研究過程中下載了一個學術論文 (pdf)，需要讀取其內容。

## 3. 技術規格 (Technical Specifications)

### 3.1 整合架構
- **目錄位置**: `src/skills/markitdown/`
- **資源管理**: 
  - 使用獨立的 Python 虛擬環境 (`.venv`) 於技能目錄內，避免全局依賴污染。
  - 核心入口點為 `SKILL.md`，定義工具調用準則。
  - 輔助腳本 `converter_wrapper.py` 用於封裝 `markitdown` 的 Python API。

### 3.2 功能限制 (Constraints & Safeguards)
- **隱私安全性**:
  - 預設禁用 LLM-based OCR 與影像描述（除非使用者明確授權並提供 API Key），以防止敏感文件上傳至雲端。
  - 所有轉換動作均在本地端 (Local) 執行。
- ** Token 效率**:
  - 禁止將二進位檔案直接上傳至 LLM Context。
  - 轉換後的 Markdown 內容若超過 10,000 tokens，應提示使用者並建議進行切分處理。
- **資源管理**:
  - 執行後應自動清理產生的暫存 Markdown 檔案，或將其儲存於專案指定的測試資料夾/暫存區。

### 3.3 工具定義 (Tool Definitions)
- `markitdown_convert`:
  - **輸入**: 檔案路徑 (absolute path)。
  - **輸出**: 轉換後的 Markdown 文本內容。
  - **參數**: `--enable-plugins` (預設為 false)。

## 4. 需求批判 (Requirements Critique)

### 第一輪：環境隔離性
- **問題**: 如何確保 Windows 環境下的 Python 虛擬環境路徑不會出錯？
- **對策**: 腳本應使用絕對路徑引用虛擬環境中的 python 解釋器，而非依賴系統 PATH 的 activate。

### 第二輪：大檔案處理
- **問題**: Excel 檔案若包含數萬列數據，轉換為 MD 後會導致 LLM 無法負荷。
- **對策**: 在 `converter_wrapper.py` 中加入大小檢查，對超過一定行數的 Excel 進行截斷或摘要。

### 第三輪：失敗處理
- **問題**: 某些 PDF 內容為純影像且未經 OCR，轉換後會是空白。
- **對策**: 檢測輸出內容是否過短，若是，則主動告知使用者此文件可能為掃描件，需開啟 OCR 模式（需授權）。

## 5. 驗證標準
1. 成功建立虛擬環境並安裝 `markitdown`。
2. 能正確將 docx 轉換為 MD，並保留標題層級。
3. 能正確將 xlsx 轉換為 MD 表格。
4. 錯誤處理：傳入不存在的路徑時應回傳清晰錯誤訊息。
