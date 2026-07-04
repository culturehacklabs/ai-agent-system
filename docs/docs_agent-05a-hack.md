# Agent 05a · Hack

*Companion to the "05a — Hack" video. What the Hack agent is, how to work with it, and what goes in and comes out.*

New to the system? Watch the "00 — Introduction" video first, and use Agent 00 for any method question. This guide assumes the agents are already installed.

> **A note on numbering.** Hack and Evaluate are one phase — **Phase 5** — split across two agents: **05a · Hack** designs the intervention, and **05b · Impact** evaluates it and routes the next cycle. Evaluate is nested inside the Hack phase, not a separate sixth phase.

---

## ✅ Before you start — install checklist (Agent 05a · Hack)

*Uses the same three file types as every agent; only the Agent KBs differ. The three Shared KBs are identical across all agents.*

**Instructions field:**

- [ ] `05a_Hack_Instructions.md`

**Agent KBs (upload):**

- [ ] `KB_05a_Hack_Module.md`
- [ ] `KB_05a_Hack_Actions_A.md`
- [ ] `KB_05a_Hack_Actions_B.md`
- [ ] `KB_05a_Hack_Prompting.md`
- [ ] `KB_05a_Hack_Tools.md`

**Shared KBs (upload — same in every agent):**

- [ ] `KB_CHL_Method.md`
- [ ] `KB_AI_Fluency.md`
- [ ] `KB_Agent_Directory.md`

*(Agent 05a's Actions KB is split in two: **A** carries the Hacking Tree's four branches, and **B** carries the Lean and Full Logistics tracks. Each loads when you reach it.)*

---

## ⬇️ Install it the quick way — the agent zip

Everything in the checklist above also ships as a single **zip** in the repo's [`install v2.0.0`](https://github.com/culturehacklabs/ai-agent-system/tree/main/install%20v2.0.0) folder. Each zip contains two folders that map straight onto the three buckets:

- **`Project Instructions (paste)`** → **bucket 1**. A single text file — open it in any text editor and paste it into the Project's **Instructions** field. *(It's the contents of `05a_Hack_Instructions.md`, saved as `.txt` so it opens on any computer without a Markdown viewer.)*
- **`Project Documents (upload)`** → **buckets 2 + 3**. All of Agent 05a's KBs *and* the three Shared KBs. Upload every file as Project knowledge.

**Five steps:** (1) download Agent 05a's zip; (2) create a new Claude Project named *"CHL Agent 05a — Hack"*; (3) paste the Instructions text into the **Instructions** field; (4) upload everything in `Project Documents (upload)`; (5) start with a prompt from `KB_05a_Hack_Prompting.md`.

Prefer to pull the files individually from the repo instead? The checklist above lists every one by name — see the [Install guide](../install.md) for the file-by-file route. The zip is just the fast path; it doesn't replace the repo.

---

## 1. What it is

**Agent 05a · Hack** turns the recoded narrative into a concrete cultural intervention — something that actually exists in the world and reaches an audience. It works through two layers: the **Hacking Tree** and the **Logistics Plan**.

The **Hacking Tree** has four branches, each building on the last:

- **Media** — what format carries the message (the one your audience already uses and shares), found through the *intersections* between audience segments.
- **Meme** — the message distilled into a shareable cultural unit (Symbols → Associations → Synthesis), pressure-tested with the SUCCESs stickiness test.
- **Tone** — the emotional strategy (Mood → Feelings → Stimuli), with one rule: the emotion must lead to agency, not trap people in feeling.
- **Hack** — where, how big, and when: Space → Scale → Moment. *Is there a wave to catch?*

Two things to hold onto:

- **This is a creative phase.** The agent brainstorms, structures, and sharpens — but the best hacks carry a human touch no tool can produce. The Hacking Tree works well as a creative brief you hand to an artist, designer, or community collaborator.
- **Ship the prototype.** The goal isn't a perfect intervention; it's a good-enough one you can launch, learn from, and improve. A hack that ships and fails teaches more than one that never launches.

---

## 2. General instructions

**Three modes:** Hacking ⚡ (default — moves through the branches, asking only for what's missing), Learning 🌱 (write "learning mode" — explains each concept, one branch at a time), and **Stand-alone 🔧** (arrive without Agent 04 outputs to design a one-off action or workshop).

**On stand-alone use:** the agent first collects a **light Audience Profile** — age, gender, location, political stance, and the shift you're seeking. **"The general public" is not accepted.** If you can't describe your audience as specific people, it helps you narrow before the Hacking Tree begins.

**How a session flows:** confirm the Agent 04 inputs (or collect the light Audience Profile) → **Media** → **Meme** → **Tone** → **Hack (Space/Scale/Moment)** → **Logistics**, choosing the *lean* track for speed or the *full* track for depth → confirm the complete Hacking Tree + Logistics Plan is ready for 05b.

*Starter prompt:* "Here's my Narrative Strategy and Recoded Narrative (with Message) from Agent 04: [paste]. Help me build the Hacking Tree."

If you get stuck, `KB_05a_Hack_Prompting.md` has stuck-point guidance for the common ones — no obvious format, a meme that isn't sticky, a tone that feels manipulative, overwhelming logistics, or not knowing when to launch.

---

## 3. Input → Output

- **Receives from 04:** Narrative Strategy · Recoded Narrative (with Message) · Audience Profile(s) (optional). *(Stand-alone: a light Audience Profile collected directly.)*
- **Produces:** the **Hacking Tree** (all four branches) · a **Logistics Plan** (lean or full) · a light documentation baseline for evaluation.
- **Passes to 05b:** the Hacking Tree + Logistics Plan, with the full documentation package travelling alongside it.

**The handoff in one line:** 04 → Narrative Strategy + Recoded Narrative (with Message) → **05a → Hacking Tree + Logistics Plan → 05b**.

---

*Built on the Culture Hack Method by [Culture Hack Labs](https://www.culturehack.io/). Part of the CHL AI Agent System. Next: Agent 05b · Impact.*
