# Agent 00 · Q&A

*Companion to the "00 — Introduction" video. Your front-door agent: what to put in its Project, and how to use it.*

New to the system? This is where to start. Agent 00 answers method questions and routes you to the right agent — it does not produce phase outputs.

---

## ✅ Install checklist — Agent 00 · Q&A

*Make sure all of these are in the Agent 00 Project before you start. (Each later agent uses the same three Shared KBs — only the Agent KBs change.)*

**Instructions field:**

- [ ] `00_QA_Instructions.md`

**Agent KBs (upload):**

- [ ] `KB_00_QA_Module.md`
- [ ] `KB_00_QA_Documentation.md`
- [ ] `KB_00_QA_Prompting.md`
- [ ] `KB_01_Ask_Module.md`
- [ ] `KB_02a_Listen_Module.md`
- [ ] `KB_02b_Research_Module.md`
- [ ] `KB_03_Understand_Module.md`
- [ ] `KB_04_Recode_Module.md`
- [ ] `KB_05a_Hack_Module.md`
- [ ] `KB_05b_Impact_Module.md`

**Shared KBs (upload — same in every agent):**

- [ ] `KB_CHL_Method.md`
- [ ] `KB_AI_Fluency.md`
- [ ] `KB_Agent_Directory.md`

*(In this agent, the Module KBs for 01 · 02a · 02b · 03 · 04 · 05a · 05b are the knowledge base of the entire methodology — that's how Agent 00 can answer questions about any phase. Agent 00 has no Tools file — it calls no external tools.)*

---

## ⬇️ Install it the quick way — the agent zip

Everything in the checklist above also ships as a single **zip** in the repo's [`install v2.0.0`](https://github.com/culturehacklabs/ai-agent-system/tree/main/install%20v2.0.0) folder. Each zip contains two folders that map straight onto the three buckets:

- **`Project Instructions (paste)`** → **bucket 1**. A single text file — open it in any text editor and paste it into the Project's **Instructions** field. *(It's the contents of `00_QA_Instructions.md`, saved as `.txt` so it opens on any computer without a Markdown viewer.)*
- **`Project Documents (upload)`** → **buckets 2 + 3**. All of Agent 00's KBs *and* the three Shared KBs. Upload every file as Project knowledge.

**Five steps:** (1) download Agent 00's zip; (2) create a new Claude Project named *"CHL Agent 00 — Q&A"*; (3) paste the Instructions text into the **Instructions** field; (4) upload everything in `Project Documents (upload)`; (5) start with a prompt from `KB_00_QA_Prompting.md`.

Prefer to pull the files individually from the repo instead? The checklist above lists every one by name — see the [Install guide](../install.md) for the file-by-file route. The zip is just the fast path; it doesn't replace the repo.

---

## How to use Agent 00 · Q&A

**Agent 00 is your front door.** It's the one to open when you're new, unsure which agent you need, or stuck on a concept. It answers questions and routes you — it does **not** produce phase outputs (no POV, no research; it sends you to the agent that does).

**What to ask it:**

- *Orientation* — "I'm new to the Culture Hack Method. Where do I start?"
- *Concepts* — "What is a frame, and how is it different from a metaphor?" · "What does the Window of Discourse mean in practice?"
- *Navigation* — "I want to decode a dominant narrative. Which agent does that?"
- *Documentation* — "What do I need to document in the Listen phase?"
- *Getting unstuck* — "I'm in the Understand phase and not sure what I should be producing. Can you clarify?"

**Two modes (in Agent 00 and every agent):**

- **Hacking Mode ⚡ (default)** — it answers directly and asks only for what's missing.
- **Learning Mode 🌱** — it explains as it goes; turn it on by writing **"learning mode"** in your message.

**How a session flows:** ask your question → Agent 00 loads only the knowledge it needs → gives you a plain-language answer → tells you which agent to open next. When it points you onward, that's your cue to move to Agent 01 and begin.

---

*Built on the Culture Hack Method by [Culture Hack Labs](https://www.culturehack.io/). Part of the CHL AI Agent System — see `INDEX.md` and `INSTALL.md` for full details. Next: Agent 01 · Ask.*
