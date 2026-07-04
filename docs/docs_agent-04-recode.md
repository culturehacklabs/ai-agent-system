# Agent 04 · Recode

*Companion to the "04 — Recode" video. What the Recode agent is, how to work with it, and what goes in and comes out.*

New to the system? Watch the "00 — Introduction" video first, and use Agent 00 for any method question. This guide assumes the agents are already installed.

---

## ✅ Before you start — install checklist (Agent 04 · Recode)

*Uses the same three file types as every agent; only the Agent KBs differ. The three Shared KBs are identical across all agents.*

**Instructions field:**

- [ ] `04_Recode_Instructions.md`

**Agent KBs (upload):**

- [ ] `KB_04_Recode_Module.md`
- [ ] `KB_04_Recode_Actions_A.md`
- [ ] `KB_04_Recode_Actions_B.md`
- [ ] `KB_04_Recode_Actions_C.md`
- [ ] `KB_04_Recode_Prompting.md`
- [ ] `KB_04_Recode_Tools.md`

**Shared KBs (upload — same in every agent):**

- [ ] `KB_CHL_Method.md`
- [ ] `KB_AI_Fluency.md`
- [ ] `KB_Agent_Directory.md`

*(Agent 04's Actions KB is split into three: **A** for audience, **B** for the decode/recode work across the eight lenses, and **C** for the narrative strategy. Each loads only when you reach that part of the workflow.)*

---

## ⬇️ Install it the quick way — the agent zip

Everything in the checklist above also ships as a single **zip** in the repo's [`install v2.0.0`](https://github.com/culturehacklabs/ai-agent-system/tree/main/install%20v2.0.0) folder. Each zip contains two folders that map straight onto the three buckets:

- **`Project Instructions (paste)`** → **bucket 1**. A single text file — open it in any text editor and paste it into the Project's **Instructions** field. *(It's the contents of `04_Recode_Instructions.md`, saved as `.txt` so it opens on any computer without a Markdown viewer.)*
- **`Project Documents (upload)`** → **buckets 2 + 3**. All of Agent 04's KBs *and* the three Shared KBs. Upload every file as Project knowledge.

**Five steps:** (1) download Agent 04's zip; (2) create a new Claude Project named *"CHL Agent 04 — Recode"*; (3) paste the Instructions text into the **Instructions** field; (4) upload everything in `Project Documents (upload)`; (5) start with a prompt from `KB_04_Recode_Prompting.md`.

Prefer to pull the files individually from the repo instead? The checklist above lists every one by name — see the [Install guide](../install.md) for the file-by-file route. The zip is just the fast path; it doesn't replace the repo.

---

## 1. What it is

**Agent 04 · Recode** is where analysis becomes strategy, and strategy becomes language. It moves through five connected moments: **Audience + Objectives**, **Decode**, **Recode**, **Message**, and **Narrative Strategy**.

The core tool is **decode → recode through eight lenses**: Verbs · Subjects & Objects · Evoked Images · Hidden Assumptions · Logic · Ideology · Metaphor · Framing. You take a paragraph-length message that carries the dominant narrative, map its hidden structure lens by lens (decode), then consciously rebuild an alternative through the same lenses (recode) — guided by who you need to reach and what shift you're after.

Two things worth knowing:

- **The Message is a message, not a slogan.** The output is one to three paragraphs — the full structure of meaning, closer to a manifesto than a tagline. The condensed cultural unit (the meme, the hashtag) comes later, in Agent 05a. If your recode comes out as a slogan, it isn't finished.
- **The recode is a new construction, not a mirror inversion.** It's built from what your audience already believes and values, not simply the opposite of the dominant frame.

---

## 2. General instructions

**Three modes:** Hacking ⚡ (default — moves through the workflow and produces outputs, asking only for what's missing), Learning 🌱 (write "learning mode" — explains each lens before you use it, one step at a time), and **Stand-alone** (arrive without Agent 03 inputs to decode/recode a single message, test your own communications, or run a workshop — it skips straight to *what message, which audience?* and treats the Narrative Strategy as optional).

**How a session flows (full path):** confirm the Agent 03 inputs and your POV → turn Agent 03's **Narrative Intentions** into committed **Narrative Objectives** (which audiences, what movement on the map, which frames to challenge/strengthen/introduce) → identify the representative message → **decode** it through the eight lenses → **recode** it into a new message → build the **Narrative Strategy** (short-term actions that become the Hacking Tree, plus long-term hypotheses) → confirm the handoff to 05a.

A key check the agent runs: **audience coherence.** A hack can't speak to two audiences that need contradictory messages — if you name incompatible audiences, it flags that as a strategic choice and helps you either choose one or plan separate decode/recode threads.

*Starter prompt:* "Here is my Agent 03 output: [paste the Community Analysis Report + Narrative Map]. Plus our POV: [paste Short POV]. Let's set audience and objectives, then decode and recode the dominant message."

If you get stuck, `KB_04_Recode_Prompting.md` has power prompts for the classic traps — no clear message to decode, a stuck metaphor lens, a recode that came out as a slogan or as a mirror inversion, and objectives with no articulated effects.

---

## 3. Input → Output

- **Receives from 03:** Community Analysis Report · Narrative Map · Window of Discourse assessment. *(Stand-alone: just a message and an audience. Iteration: your previous Narrative Strategy and Recoded Narrative.)*
- **Produces:** **Narrative Strategy** · **Recoded Narrative (with Message)** · **Audience Profile(s)** (optional, empathy-map format).
- **Passes to 05a:** the Narrative Strategy + the Recoded Narrative (with Message), plus any Audience Profile(s).

**The handoff in one line:** 03 → Community Analysis Report + Narrative Map → **04 → Narrative Strategy + Recoded Narrative (with Message) → 05a**.

---

*Built on the Culture Hack Method by [Culture Hack Labs](https://www.culturehack.io/). Part of the CHL AI Agent System. Next: Agent 05a · Hack.*
