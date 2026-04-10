---
name: antigravity-manual
description: Antigravity 官方使用說明書 (本機全域版)。包含核心概念、代理配置、安全沙箱、擴充功能與工具子代理的深度指南。
---

# Antigravity 全域操作指南

歡迎調用 Antigravity 官方說明 Skill。本技能旨在提供關於系統架構與配置的準確權威定義。

> [!TIP]
> **官方參考連結 (Official Source)**: [Antigravity Documentation](https://antigravity.google/docs/get-started)

## 📖 指南索引 (Branch Directory)

當您需要了解特定主題時，請優先打開對應的連結檔案：

1.  **[核心概念 (Core Concepts)](docs/01-core-concepts.md)**
    *   內容：介面定義（Editor/Browser/Manager）、關鍵術語（Agent/Tab/Command）、基礎架構與系統需求。
2.  **[代理配置 (Agent Configuration)](docs/02-agent-configuration.md)**
    *   內容：代理模式（Planning/Fast）、支援模型清單（Gemini/Claude/OSS）、MCP 協定與自定義設定。
3.  **[權限與安全 (Permissions & Security)](docs/03-permissions-security.md)**
    *   內容：動作白名單格式（command/read_file/read_url）、沙箱等級與設定、隱私與隱含記憶。
4.  **[擴充功能開發 (Extensibility)](docs/04-extensibility-workflows.md)**
    *   內容：如何撰寫規則 (Rules)、建立工作流 (Workflows) 與開發標準技能 (Skills)。
5.  **[原生工具與瀏覽器 (Native Tools)](docs/05-native-tools-browsing.md)**
    *   內容：瀏覽器子代理 (Browser Subagent) 的運作機制、螢幕擷取、終端機與檔案系統操作指引。

## 🛠️ 調用準則 (Usage Guidelines)

*   **優先查閱**：在修改全域設定 (`GEMINI.md`) 或工作區規則前，必須先查閱相關章節以確保路徑與語法符合系統規範。
*   **拒絕猜測**：如果對某個功能的權限格式或行為有疑問，請直接 `view_file` 打開上述文件，嚴禁憑空推測。
*   **繁體中文輸出**：回應使用者關於 Antigravity 的技術諮詢時，請使用繁體中文，並引用本手冊中的術語。
