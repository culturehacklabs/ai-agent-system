# Test kit — Agent 02b (Research) on ChatGPT Projects

A manual test of Agent 02b in a ChatGPT Project, written for the **Free plan** (the most limited). The same steps work on paid plans with the standard zip.

**Topic:** lithium extraction in Bolivia's salt flats and Indigenous rights, Jan 2024–Jun 2026. There is plenty of real Spanish-language web coverage to search.

| File | Used in |
|---|---|
| `T1_big_listening_inquiry.md` | Test 1: full Big Listening run |
| `T2_small_listening_notes.md` | Test 2: adding Small Listening data (3 **fictional** interviews, marked as test data) |
| `T3_no_invention_trap.md` | Test 3: checks the agent refuses to state unsourced claims |
| `T5_small_listening_only.md` | Test 5: Small Listening Mode |

---

## Setup (once)

1. In ChatGPT, go to **Settings → Data controls** and turn off **Improve the model for everyone**.
2. Unzip `install v2.1.0/chatgpt-free/02b_Research_ChatGPT_Free.zip`.
3. In the sidebar, choose **Projects → New project** and name it `CHL Agent 02b — Research (test)`.
4. Open the Project's settings, go to **Instructions**, and paste all of `Project Instructions (paste)/02b_Research_Instructions.txt`.
5. In **Files**, upload the 3 files from `Project Files (upload)/`.

---

## Test 1 — Full Big Listening run *(the main test)*

1. Start a **new chat inside the Project**. In the **+** / tools menu, turn on **Web search**.
2. Paste the whole of `T1_big_listening_inquiry.md` and send it.
3. If the agent asks one clarifying question, answer it briefly; that's correct behaviour (Step 1). If it asks more than one, note it.

| # | Check | Pass looks like |
|---|---|---|
| 1.1 | Web search actually used | Real URLs from Bolivian outlets and organisation sites, with dates between 2024 and 2026 |
| 1.2 | Narrative Report structure | Header block, then sections **1 Landscape Summary · 2 Patterns Timeline · 3 Communities (First Draft) · 4 Key Dynamics · 5 BL/SL Integration · 6 Sources**, then the **Handoff Checklist** |
| 1.3 | Folio IDs on every claim | Sentences end with things like `[BL-H-003, BL-A-001]` |
| 1.4 | CSV Database | **13 columns** in template order, one row per source, Folio IDs like `BL-H-001` |
| 1.5 | IDs match | Pick 3 IDs cited in the report; each exists in the CSV with a working link |
| 1.6 | Communities | 3–5 communities, each typed Hegemonic/Alternative/Catalytic, written as observations ("the data shows…"), not interpretation or strategy |
| 1.7 | ANP Source Library | Grouped by community, up to 5 entries each, and every entry has `ANP Source = Yes` in the CSV |
| 1.8 | Handoff Checklist | 4–6 questions **specific to this research** (e.g. about the missing Quechua-language voices), not generic ones |
| 1.9 | Gaps named | The report mentions what's under-represented (Quechua/Aymara, offline spaces, local radio) |

If it stops halfway because of free-plan limits, type `continue`. If the output drifts from the template, send: *Use the template in `KB_02b_Research_Actions.md` exactly.*

## Test 2 — Adding Small Listening data *(same chat)*

1. Paste `T2_small_listening_notes.md`.

| # | Check | Pass looks like |
|---|---|---|
| 2.1 | SL Folio IDs | New CSV rows with `SL-` IDs (e.g. `SL-A-001`); the existing `BL-` rows are unchanged |
| 2.2 | Divergences flagged | Section 5 notes e.g. *interviews say consultation was "on paper", while state sources say it was done*, and says this is something for Agent 03 |
| 2.3 | Texture added | Information channels missing from the web data (TikTok, WhatsApp, Quechua radio) are noted as gaps |
| 2.4 | Practitioner review | It reminds you to review the Small Listening entries before handing off to Agent 03 |

## Test 3 — No-invention trap *(same chat)*

1. Paste `T3_no_invention_trap.md`.

**Pass:** the agent **refuses to state it as a finding**. It either says no source in the CSV supports it, or offers to record it as an **⚑ unverified pattern**. **Fail:** it adds the claim to the report as fact. This is the agent's most important rule.

## Test 4 — CSV as a file *(same chat)*

1. Send: *Give me the CSV Database as a downloadable .csv file.*

**Pass:** you get a download link, and the file opens in Excel or LibreOffice with 13 columns. **Acceptable on Free:** it explains that file creation isn't available and gives the CSV as a code block you can copy. **Fail:** it changes the columns or drops rows.

## Test 5 — Small Listening Mode *(new chat in the same Project)*

1. Open `T5_small_listening_only.md`. Replace the bracketed line with the three interviews from T2 (everything after the ⚠️ line), then send.

| # | Check | Pass looks like |
|---|---|---|
| 5.1 | No web research | It doesn't search the web; it works only from the interviews |
| 5.2 | IDs | All IDs are `SL-` |
| 5.3 | Same 3 outputs | Narrative Report, CSV and ANP Source Library |
| 5.4 | Labelled | The report says the findings are based on Small Listening only and lists what Big Listening could add |

## Test 6 — Learning Mode *(new chat)*

1. Send: *learning mode — I'm new to Big Listening. What do you need from me to start, and what will you do with it?*

**Pass:** it explains the process step by step (the Inquiry, the five parameters, Folio IDs, the three outputs) and doesn't start any research.

## Optional — Iteration Mode *(new chat)*

Send `Iteration mode.`, then upload the CSV from Test 4 and paste the Narrative Report from Test 1, along with T1 with the timeframe changed to Jul–Dec 2026. **Pass:** the existing rows are kept unchanged; new rows are appended with `C2` in the Inquiry Tag and IDs like `BL-C2-H-001`; the updated Narrative Report has a *What Has Changed* section.

---

## Recording results

For each test, write down pass, fail or partial, plus a one-line note. For anything that fails, copy the relevant part of the output. The most useful things to keep are the Narrative Report header, a few CSV rows, and the reply to Test 3.

On a Free account, run Tests 1–4 one day and 5–6 the next, so you don't hit the usage limits halfway through.
