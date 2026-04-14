# Antigravity Feedback Flywheel (回饋飛輪紀錄)

本文件用於捕捉 **Developer Judgment** 作為信號的即時紀錄。每次使用者對 Agent 的方向進行修正、或是啟動子代理進行驗證後，應在此記錄原因與模式，以作為未來「靜態化 (Staticize)」為系統規則的基礎。

---

## 🔄 飛輪紀錄表

| 日期 | 場景 (Scenario) | 使用者修正/決策 (Judgment Signal) | 潛在規則 (Potential Static Rule) | 狀態 |
| :--- | :--- | :--- | :--- | :--- |
| 2026-04-14 | 升級動態代理架構 | 同意導向 T2 動態分解與子代理機制 | 高風險任務強制提議啟動 Sub-agent | [x] 已加入 Skill |
| 2026-04-14 | 全域移植性考量 | 提出模板不應寫死在 Infra 專案，應確保全域皆可使用 | 將模板編碼進 Skill (Embedded)，並在 GEMINI.md 加入自動收集規則 | [x] 已全域部署 |
| 2026-04-14 | 全域晉升機制 | 指出全域規則也應隨專案修正而更新 | 建立本地 Flywheel -> 全域 GEMINI.md 的晉升路徑 | [x] 已加入 Protocol |
| 2026-04-14 | 專案整潔度 (Hygiene) | 提議區分「核心資產 (憲法/飛輪)」與「臨時文件 (計畫/任務)」的 Git 管理 | 建議 ignore 臨時文件，但 commit 核心憲法與飛輪 | [x] 已加入 Skill |

---

## 🛠️ 維護準則
1. **即時性**：在對話中發生重大方向修正後，AI 應主動更新此表。
2. **靜態化觸發**：當同一類型的「使用者修正」出現超過 **3 次**，或累積 **5 筆** 不同紀錄時，AI 應提議更新 `GEMINI.md` 或相關 `SKILL.md`。
3. **目的**：減少未來的 Friction，讓 Static Scaffolding 越來越準。
