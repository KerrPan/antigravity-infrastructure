# 代理配置與模型支援 (Agent Configuration)

Antigravity 允許使用者根據任務需求靈活調整代理的行為模式與所使用的模型。

## 1. 代理模式 (Agent Modes)
代理主要有兩種運行模式：
*   **規劃模式 (Planning Mode)**：適用於複雜、多步驟的任務。代理會先進行「研究 (Research)」並產出「實作計畫 (Implementation Plan)」，經使用者核准後再執行。這種模式更嚴謹，能有效防止盲目變更。
*   **快速模式 (Fast Mode)**：適用於即時、簡單的指令或是回答問題。省略詳細規劃，直接提供回應或執行操作。

## 2. 支援模型 (Supported Models)
系統整合了多款頂尖推理模型，可供切換：
*   **Gemini 系列**：
    *   **Gemini 3.1 Pro**：最強大的推理模型，支援多模態輸入與超長上下文。具備 High (高效能) 與 Low (省資源) 兩種資源配置。
    *   **Gemini 3 Flash**：反應速度極快，適合處理簡單的快速任務。
*   **Claude 系列**：
    *   **Claude 4.6 Sonnet (Thinking)**：具備優異的邏輯推理與代碼理解能力。
    *   **Claude 4.6 Opus (Thinking)**：最強效能模型，適合處理極高難度的架構設計。
*   **開源模型**：
    *   **GPT-OSS-120b**：本地化或開源環境的首選，平衡了效能與隱私。

## 3. 進階配置
*   **MCP (Model Context Protocol)**：代理可透過 MCP 存取外部工具與數據源，擴展其認知與操作邊界。
*   **自定義設定**：使用者可在 `Agent Settings` 中調整模型的溫度 (Temperature)、最大輸出長度等參數。
