# Agent 05b · Impact

*Companion to the "05b — Impact" video. What the Impact & Iteration agent is, how to work with it, and what goes in and comes out.*

New to the system? Watch the "00 — Introduction" video first, and use Agent 00 for any method question. This guide assumes the agents are already installed.

> **A note on numbering.** Hack and Evaluate are one phase — **Phase 5** — split across two agents: **05a · Hack** designs the intervention, and **05b · Impact** evaluates it and routes the next cycle. Evaluate is nested inside the Hack phase, not a separate sixth phase.

---

## ✅ Before you start — install checklist (Agent 05b · Impact)

*Uses the same three file types as every agent; only the Agent KBs differ. The three Shared KBs are identical across all agents. Agent 05b has **no Tools KB** — don't go looking for one.*

**Instructions field:**

- [ ] `05b_Impact_Instructions.md`

**Agent KBs (upload):**

- [ ] `KB_05b_Impact_Module.md`
- [ ] `KB_05b_Impact_Actions_A.md`
- [ ] `KB_05b_Impact_Actions_B.md`
- [ ] `KB_05b_Impact_Actions_C.md`
- [ ] `KB_05b_Impact_Actions_D.md`
- [ ] `KB_05b_Impact_Prompting.md`

**Shared KBs (upload — same in every agent):**

- [ ] `KB_CHL_Method.md`
- [ ] `KB_AI_Fluency.md`
- [ ] `KB_Agent_Directory.md`

*(Agent 05b's Actions KB is split into four, one per output: **A** the Pre-Hack Documentation Plan, **B** the Post-Hack Evaluation, **C** the Hack Database — which is also the home of the full documentation database for the whole system — and **D** the Case Study.)*

---

## ⬇️ Install it the quick way — the agent zip

Everything in the checklist above also ships as a single **zip** in the repo's [`install v2.0.0`](https://github.com/culturehacklabs/ai-agent-system/tree/main/install%20v2.0.0) folder. Each zip contains two folders that map straight onto the three buckets:

- **`Project Instructions (paste)`** → **bucket 1**. A single text file — open it in any text editor and paste it into the Project's **Instructions** field. *(It's the contents of `05b_Impact_Instructions.md`, saved as `.txt` so it opens on any computer without a Markdown viewer.)*
- **`Project Documents (upload)`** → **buckets 2 + 3**. All of Agent 05b's KBs *and* the three Shared KBs. Upload every file as Project knowledge. *(There is no Tools file in this folder — that's expected.)*

**Five steps:** (1) download Agent 05b's zip; (2) create a new Claude Project named *"CHL Agent 05b — Impact"*; (3) paste the Instructions text into the **Instructions** field; (4) upload everything in `Project Documents (upload)`; (5) start with a prompt from `KB_05b_Impact_Prompting.md`.

Prefer to pull the files individually from the repo instead? The checklist above lists every one by name — see the [Install guide](../install.md) for the file-by-file route. The zip is just the fast path; it doesn't replace the repo.

---

## 1. What it is

**Agent 05b · Impact** is the closing and opening of the cycle: it helps you document the hack, evaluate what shifted, and feed what you learned back in. It answers one central question — *is the narrative space being rewilded?*

It has **four outputs**, and they are not all required. You choose based on where you are:

- **A — Pre-Hack Documentation Plan** — built *before* launch: baseline capture, monitoring setup, evaluation calendar.
- **B — Post-Hack Evaluation** — built *after* the hack: the three-level impact evaluation plus an iteration strategy. This alone is enough to keep hacking.
- **C — Hack Database** — a living full-cycle record you can build or update at any time. It's also where the system's full documentation database lives.
- **D — Case Study** — a publishable narrative for movement learning (needs C, or equivalent documentation, first).

Evaluation runs on **three levels**: **Audience Impact** (reach, response, adoption — weeks to months), **Discourse Impact** (change against the Agent 03 ANP baseline — months), and **Systems Change Contribution** (tipping-point conditions — years). Every evaluation closes with three personal reflection questions — the implications of the work for **you**, your **community**, and the **planet**. These are human co-creation moments; the agent can help you think them through, but the answers are yours.

The agent never blocks iteration behind documentation. Output B is always enough to move on.

---

## 2. General instructions

**Two modes:** Hacking ⚡ (default — produces outputs efficiently, asking only for what's missing) and Learning 🌱 (write "learning mode" — a structured, one-question-at-a-time interview, especially useful for reconstructing a past hack for the Hack Database when you don't have full documentation).

**How a session flows:** the agent first asks **where you are** — hack not yet launched (→ A), hack completed (→ B, then offers C and D), documenting the full cycle (→ C), or ready to publish (→ D) → it confirms whatever inputs you have (Agent 05a Hacking Tree + Logistics, Agent 04 hypotheses, Agent 03 baseline, POV) → produces the requested output → names what comes next.

*Starter prompt (after a hack):* "The hack is done. Here's what happened: [paste documentation or description]. Help me evaluate the impact."

If you get stuck, `KB_05b_Impact_Prompting.md` has guidance for the common situations — no pre-hack baseline, thin results (thin results are real results), contradictory A/B versions, or answering the three closing questions.

---

## 3. Input → Output

- **Receives from 05a:** Hacking Tree · Logistics Plan · documentation baseline. **Also draws on:** Agent 04's hypotheses, Agent 03's community map + ANP baseline, and the POV from Agent 01.
- **Produces:** **(A) Pre-Hack Documentation Plan · (B) Post-Hack Evaluation + Iteration Strategy · (C) Hack Database · (D) Case Study.**
- **Passes on:** the **Post-Hack Evaluation** carries an explicit iteration strategy that routes you to the right agent for the next cycle — most often back to **Agent 02a** (update the Listening Model) or **Agent 04** (revise the strategy). You don't restart at Agent 01; the POV is refined, not rebuilt.

**The handoff in one line:** 05a → Hacking Tree + Logistics Plan → **05b → Post-Hack Evaluation + Case Study → back to Agent 02a or 04**.

That's the full cycle. Each turn — launch, monitor, evaluate, adapt, relaunch — sharpens the strategy and increases the chance of shifting the narrative space.

---

*Built on the Culture Hack Method by [Culture Hack Labs](https://www.culturehack.io/). Part of the CHL AI Agent System. The cycle continues — return to Agent 02a or Agent 04 to begin the next turn.*
