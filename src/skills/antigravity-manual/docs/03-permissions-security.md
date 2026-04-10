# 權限、安全與沙箱 (Permissions & Security)

Antigravity 採用極為嚴格的安全機制，確保 AI 在受控且安全的環境下運行。

## 1. 動作白名單 (Action Whitelist)
代理在執行任何操作（如讀取檔案、執行指令）前，系統會檢查權限清單。常見權限格式如下：
*   **指令執行**：`command(prefix)` 或 `command(*)`（允許所有）。
*   **檔案存取**：`read_file(/path)` 或 `write_file(/path)`。請注意，寫入權限自動包含讀取權限。目前路徑須為絕對路徑。
*   **網路存取**：`read_url(domain)` 或 `read_url(*)`，支援網域及其子網域匹配。
*   **MCP 存取**：`mcp(server/tool)` 指定可調用的模型上下文協定工具。

## 2. 沙箱機制 (Sandboxing)
為了防止惡意或誤操作影響主機系統，Antigravity 提供核心級別的隔離技術：
*   **macOS**：使用 Seatbelt (`sandbox-exec`) 技術。
*   **Linux**：使用 `nsjail` 容器化技術。
*   **管控範疇**：沙箱會嚴格限制代理對終端機、網路、及非授權檔案系統的存取。
*   **狀態設定**：沙箱預設為 **禁用 (Disabled)**，建議在處理未知或複雜專案時手動開啟；網路部分亦可透過 `Sandbox Allow Network` 額外控制。

## 3. 隱私與隱含記憶 (Privacy & Implicit Memory)
*   系統會根據使用習慣產生隱含記憶，以優化個人化體驗。
*   使用者可以隨時查閱或刪除這些記憶，確保 AI 的「長期記憶」在您的掌控之中。
