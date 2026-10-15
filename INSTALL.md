# INSTALL — Deploying the CHL AI Agents

This guide explains how to set up and use the CHL AI Agent System across different platforms and contexts.

---

## How the Agent Architecture Works

Each agent is built from two types of files:

**Instructions file** (`[ID]_Instructions.md`)
This is the **system prompt** — the agent's identity, operating modes, workflow, and KB load logic. In any platform, this is what you paste into the system prompt field.

**Knowledge Base files** (`KB_[ID]_*.md`)
These are the **reference documents** the agent draws on: phase theory, output templates, prompt library, tool guidance. In Claude Projects they are uploaded as project files. In other contexts they are pasted into the conversation when needed.

The split is intentional: the Instructions file is lean and stable; the KB files are modular and loaded on demand.

**A note on file sets:** the KB set is not identical across agents. Some agents split their Actions KB (Agent 04: A/B/C; Agent 05a: A/B; Agent 05b: A/B/C/D), and some add specialised KBs (Agent 02a: `KB_02a_Listen_SmallListening.md`; Agent 02b: `KB_02b_Research_MultiInquiry.md`; Agent 03: `KB_03_Understand_MapCheck.md`). Agent 05b has **no Tools file**. Always deploy the files that actually exist for that agent — see `INDEX.md` for the authoritative per-agent file list. If you install from the agent zip (below), the right set is already bundled.

---

## Option 1 — Claude Projects, from the agent zip (Recommended)

Each agent ships as a single **`.zip`** in the repo's [`install v2.1.0`](https://github.com/culturehacklabs/ai-agent-system/tree/main/install%20v2.1.0) folder. Each agent becomes its own Project.

### What's in the zip

Every zip contains exactly two folders:

| Folder | Contains | Goes to |
|--------|----------|---------|
| **`Project Instructions (paste)`** | The agent's Instructions, saved as a `.txt` file so it opens in any text editor on any computer. | Pasted into the Project **Instructions** field. |
| **`Project Documents (upload)`** | All of the agent's `KB_[ID]_*.md` files **plus** the three shared KBs (`KB_CHL_Method.md`, `KB_AI_Fluency.md`, `KB_Agent_Directory.md`). | Uploaded as Project knowledge. |

The `.txt` in the paste folder is a zip convenience only — it is the same content as the agent's canonical `[ID]_Instructions.md`. The repo and documentation always refer to the `.md` files.

### Setup steps

**1. Download and unzip** the agent's zip from the [`install v2.1.0`](https://github.com/culturehacklabs/ai-agent-system/tree/main/install%20v2.1.0) folder.

**2. Create a new Project in Claude** — name it after the agent (e.g. "CHL Agent 01 — Ask").

**3. Set the system prompt** — open the file in `Project Instructions (paste)` and paste its contents into the Project "Instructions" field.

**4. Upload the documents** — upload everything in `Project Documents (upload)` as Project knowledge (the agent's KBs and the three shared KBs together).

The Instructions file tells the agent which KBs to load for which task — you do not need to paste them manually.

**5. Test with a starter prompt** from the agent's `KB_[ID]_Prompting.md` (where present).

### Installing file-by-file instead

You don't have to use the zip. Pull the files straight from the repo per `INDEX.md`: paste the `[ID]_Instructions.md` into the Instructions field, then upload the agent's own `KB_[ID]_*.md` files (Module, Actions or Actions_A/B/C…, Prompting and Tools **where they exist**, and any specialised KBs) plus the three shared KBs. The zip is the fast path, not a replacement for the repo.

**Maintainers:** the zips are generated from `agents/`. After editing any agent file, run `python3 scripts/build_install_zips.py` to rebuild them.

### Repeat for each agent
Each agent has its own Project. Handoffs are manual: copy the output from one agent's conversation and paste it into the next agent's Project as input.

---

## Option 2 — ChatGPT Projects

The same zip works in ChatGPT. Each agent becomes its own **ChatGPT Project**: the Instructions file goes into the Project's instructions and the Documents folder goes into the Project's files. Projects are available on every ChatGPT plan, including Free.

### Setup steps

**1. Turn off training on your data** — in *Settings → Data controls*, turn off *Improve the model for everyone*. This matters for Small Listening material such as interview transcripts.

**2. Download and unzip** the agent's zip, as in Option 1.

**3. Create a Project** — in the sidebar, *Projects → New project*. Name it after the agent (e.g. "CHL Agent 01 — Ask").

**4. Instructions** — open the Project's settings and paste the contents of the file in `Project Instructions (paste)` into **Instructions**. Every Instructions file is kept under 8,000 characters.

**5. Files** — add the files in `Project Documents (upload)` to the Project's **Files**. Check the file count against your plan:

| Agent | 00 | 01 | 02a | 02b | 03 | 04 | 05a | 05b |
|-------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Files | 13 | 7 | 8 | 8 | 8 | 9 | 8 | 9 |

| Plan | Free | Go / Plus | Pro / Business / Enterprise |
|------|:--:|:--:|:--:|
| Files per Project* | 5 | 25 | 40 |

\*Limits at the time of writing; OpenAI changes them, so check the *File Uploads FAQ* in the ChatGPT help center if an upload is refused.

**On the Free plan**, every agent has more than 5 files, and Free accounts can also only upload a few files per day. Combine the KB files into 3–5 text files before uploading. Keep each original file name as a heading, so the agent can still find files by name:

```
# FILE: KB_02b_Research_Module.md
[contents of KB_02b_Research_Module.md]

# FILE: KB_02b_Research_Actions.md
[contents of KB_02b_Research_Actions.md]
```

A good grouping: (1) Module + Actions, (2) the agent's remaining KBs, (3) the three shared KBs.

**6. Tools** — Projects don't have a fixed capabilities setting; turn tools on in the chat (the **+** / tools menu in the message box) when an agent needs them:

| Agent | Web search | Code / data analysis | Why |
|-------|:---:|:---:|-----|
| 00 · Q&A | — | — | Answers from the knowledge only |
| 01 · Ask | — | — | Elicitation, no tools |
| 02a · Listen | — | — | Design only — research runs in 02b |
| **02b · Research** | **on** | **on** | Big Listening needs web search; code/data analysis delivers the CSV Database as a downloadable file and reads a previous CSV in Iteration Mode |
| 03 · Understand | — | on | Reads the 02b CSV; plots the Narrative Map when Mermaid doesn't render |
| 04 · Recode | — | — | |
| 05a · Hack | — | — | |
| 05b · Impact | — | optional | Useful if you upload metrics or survey data |

Tool availability and usage limits are lower on the Free plan; if code/data analysis isn't available, the CSV comes as a table instead of a file.

**7. Test** with a starter prompt from the agent's `KB_[ID]_Prompting.md`, in a new chat inside the Project.

### Differences from Claude Projects

- **Knowledge is searched, not read in full.** ChatGPT (like many assistant platforms with uploaded files) retrieves relevant passages from the Project's files rather than keeping every file in view. The Instructions tell the agent to look up files by name and follow templates exactly, but if an output drifts from its template, ask: *"Use the template in `KB_[file].md` exactly."*
- **Research tools.** Agent 02b uses ChatGPT web search in place of Exa Search MCP. For deeper research runs you can use Deep Research and paste the results into Agent 02b, which assigns Folio IDs and builds the CSV. See `KB_02b_Research_Tools.md` for the full tool mapping.
- **Handoffs.** Manual, as in Claude: copy the output from one agent's Project and paste it into a chat in the next agent's Project.

### A note on Custom GPTs

Earlier ChatGPT setups used Custom GPTs. Creating new GPTs is no longer available on personal ChatGPT accounts (Free, Go, Plus, Pro), and OpenAI has announced plans to retire Custom GPTs. If your Business, Enterprise, or Edu workspace still allows them, the same mapping applies — Instructions file → *Instructions*, Documents folder → *Knowledge*, tools from the table above → *Capabilities* — but prefer Projects for anything you want to keep using.

---

## Option 3 — Other LLM Services (Gemini, Mistral, etc.)

The agents are model-agnostic, and the zip contents work the same here — the Instructions file is the system prompt, the Documents folder is the knowledge. Paste the Instructions file as the system prompt, then paste the relevant KB files into the conversation as context (Module KB always; Actions KB when producing outputs). Paste `KB_CHL_Method.md` for methodology questions and `KB_Agent_Directory.md` for navigation.

If the service supports custom assistants with uploaded knowledge (e.g. Gemini Gems), follow the ChatGPT pattern in Option 2 instead: Instructions as the assistant's instructions, Documents folder as its knowledge, web search on for Agent 02b.

---

## Option 4 — Self-Hosted LLMs (Ollama, LM Studio, etc.)

Same approach, same zip contents: Instructions as system prompt, KB files as context.

### Important note for Agent 02b (Research)
Agent 02b executes Big Listening. The Claude-native version uses **Exa Search MCP** and **Claude Research Mode**. On a self-hosted LLM or a service without web access:
- Run web research manually and paste results in, or
- Use a separate research tool (Perplexity, Tavily, SerpAPI, etc.) and bring outputs into the agent, or
- Configure a web-search tool / RAG pipeline and update `KB_02b_Research_Tools.md` accordingly.

The 02b KBs describe the *process and outputs* — what to collect, how to structure the CSV — regardless of which tool searches. Swap the tool, keep the process.

---

## Option 5 — Single-Chat Use (No Project Setup)

Run any agent in one conversation: paste a brief version of the Instructions, then paste the Module + Actions KBs you need, then your input. Works well for one-off tasks and workshops.

**Works well in single-chat:** POV development (01), Decode/Recode of a message (04 stand-alone), Hacking Tree for a campaign action (05a stand-alone), case study reconstruction (05b).
**Works less well:** Agent 02b (web research tools unavailable without separate configuration) and Agent 03 (full ANP analysis works best with the complete KB set and iterative conversation).

---

## Passing Outputs Between Agents

Handoffs are manual — copy outputs from one agent and paste them into the next.

| From | Passes | To |
|------|--------|----|
| Agent 01 | Short POV | Agent 02a |
| Agent 02a | Big Listening Inquiry | Agent 02b |
| Agent 02b | Narrative Report + CSV Database + ANP Source Library | Agent 03 |
| Agent 03 | Community Analysis Report + Narrative Map (incl. Narrative Intentions + Window of Discourse) | Agent 04 |
| Agent 04 | Narrative Strategy + Recoded Narrative (with Message) + Audience Profile(s) | Agent 05a |
| Agent 05a | Hacking Tree + Logistics Plan | Agent 05b |
| Agent 05b | Case Study + updated POV | Agent 02a or 04 |

A simple preamble helps orient the next agent:

```
Here is the output from the previous phase:

[paste output]

I'm ready to continue to [next phase]. Additional context: [context]
```

---

## Shared KBs — When to Load

Loaded conditionally, never by default:

| File | Load when |
|------|-----------|
| `KB_CHL_Method.md` | Methodology, narrative theory, political stance, or the method's foundations |
| `KB_AI_Fluency.md` | Ethical AI use, data responsibility, the 4Ds framework |
| `KB_Agent_Directory.md` | Navigating between agents, confirming handoffs, checking I/O contracts |

---

## Phased Rollout (current)

All eight agents (00, 01, 02a, 02b, 03, 04, 05a, 05b) are deployment-ready at v2.1.0, which adds ChatGPT Projects setup (Option 2) and expands guidance for other LLM services (Option 3). Deploy any agent as needed; handoffs between them remain manual.

---

## Tips for Effective Use

**Be specific about context.** Vague inputs produce vague outputs.
**Use the prompt library** where it exists (`KB_[ID]_Prompting.md`).
**Iterate, don't perfect.** Every phase has an iteration workflow.
**The agent is a collaborator, not a decision-maker.** Community knowledge, political judgment, and creative vision are yours.

---

*For the full agent and file index, see [`INDEX.md`](INDEX.md).*

*v2.1.0 · updated 2026-10-14 · CHL AI Agent System.*
