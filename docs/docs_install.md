# Install

*How to set each agent up as its own project. The pattern is identical for every agent — only the middle group of files changes.*

Each agent becomes its own **Project** in Claude. A Project holds a system prompt plus reference files the agent reads automatically. There are two ways to get an agent's files in: **download its zip** (the quick way) or **pull the files individually** from the repo. Both end up in exactly the same place.

**Accounts.** You can create Projects on a free Claude account (currently capped at around five). If you'll run the full cycle regularly, a paid plan gives more Projects and higher usage. [**Always turn off**](https://claude.ai/new#settings/data-privacy-controls) **metadata location and data sharing** so your personal information isn't used to train other models. Sign up at claude.ai.

## The three kinds of file

Every agent is built from three kinds of file. The structure is identical for every agent — only the middle group changes.

| File type | What it is | Where it goes |
| ----- | ----- | ----- |
| **1 · Instructions** (`[ID]_Instructions.md`) | The agent's identity, modes, and workflow — its "brain." One per agent. | Pasted into the Project's **Instructions / system prompt** field. |
| **2 · Agent KBs** (`KB_[ID]_*.md`) | This agent's own reference files — phase theory, output templates, prompts, tools. *This is the only group that differs between agents.* | **Uploaded** as Project knowledge. |
| **3 · Shared KBs** (3 files) | The same three files in **every** agent: `KB_CHL_Method.md`, `KB_AI_Fluency.md`, `KB_Agent_Directory.md`. | **Uploaded** as Project knowledge. |

## Option 1 — Claude Projects, from the agent zip (recommended)

Each agent ships as a single **`.zip`** in the repo's [`install v2.0.0`](https://github.com/culturehacklabs/ai-agent-system/tree/main/install%20v2.0.0) folder. Inside every zip are exactly two folders, and they map cleanly onto the three file types above:

| Zip folder | Maps to | What's inside |
| ----- | ----- | ----- |
| **`Project Instructions (paste)`** | file type **1** | One text file — the agent's Instructions, saved as `.txt` so it opens in any text editor on any computer. |
| **`Project Documents (upload)`** | file types **2 + 3** | All of the agent's `KB_[ID]_*.md` files *plus* the three Shared KBs. |

The `.txt` in the paste folder is a convenience for the zip only — it's the same content as the agent's `[ID]_Instructions.md`. The repo and this documentation always refer to the canonical `.md` files.

### Setup steps

1. **Download the agent's zip** from the [`install v2.0.0`](https://github.com/culturehacklabs/ai-agent-system/tree/main/install%20v2.0.0) folder and unzip it.
2. **Create a new Project in Claude** — name it after the agent (e.g. *"CHL Agent 01 — Ask"*). *(This is shown in Claude, but the pattern — system prompt + knowledge files — works in any tool.)*
3. **Paste the Instructions.** Open the text file in `Project Instructions (paste)` and paste its contents into the Project's **Instructions** field.
4. **Upload the Documents.** Upload everything in `Project Documents (upload)` as Project knowledge — the Agent KBs and the three Shared KBs together.
5. **Test it** with a starter prompt from the agent's `KB_[ID]_Prompting.md` (where present).

The Instructions file tells the agent which KBs to load for which task — you don't need to paste them manually. Repeat for each agent; each gets its own Project. Handoffs are manual (see below).

### Prefer to install file-by-file?

You don't have to use the zip. Every agent page lists its exact three-bucket checklist by filename, and the per-agent file set is authoritative in `INDEX.md`. Pull those files straight from the repo, paste the `[ID]_Instructions.md` into the Instructions field, and upload the rest as Project knowledge. The zip is just the fast path — it doesn't replace the repo.

**A note on file sets:** the KB set is not identical across agents. Some split their Actions KB (Agent 04: A/B/C; Agent 05a: A/B; Agent 05b: A/B/C/D), some add a specialised KB (Agent 02a: `KB_02a_Listen_SmallListening.md`; Agent 02b: `KB_02b_Research_MultiInquiry.md`; Agent 03: `KB_03_Understand_MapCheck.md`), and one has no Tools file (Agent 05b). Always use the files that actually exist for that agent — the zip already contains the right set.

## Moving between agents is manual

When an agent finishes, copy its output and paste it into the next agent's Project as input, with a short preamble:

```
Here is the output from the previous phase: [paste output]
I'm ready to continue to [next phase]. Additional context: [context]
```

## Using other tools

The zip contents work the same everywhere — the Instructions file is the system prompt, the Documents folder is the knowledge. Only the loading mechanism changes.

**Other chatbots (Gemini, ChatGPT).** The agents are model-agnostic: paste the Instructions file as the system prompt / custom instruction, then paste the knowledge files into the project or chat as needed — the Module always, the Actions file when producing an output. *(Note: Agent 02b's live research uses the Exa Search connector in Claude; elsewhere, run research with a separate tool and paste results in.)*

**Local LLMs (Ollama, Hugging Face).** The system is model-agnostic and designed to work with local inference. Pair a local inference system (like Ollama) with a Web UI platform (like Open WebUI) to recreate the "Claude Project" capacity: the Instructions file becomes the system prompt and the KBs become the memory. Every KB is designed to stay under 2–4k tokens, to allow local use of the agents for technological autonomy.

**Single-chat use.** For a one-off task or a workshop, run an agent in a single conversation: paste a brief version of the Instructions, then paste the Module + Actions KBs you need, then your input. Works well for POV development (01), stand-alone decode/recode (04), a stand-alone Hacking Tree (05a), and case-study reconstruction (05b).

---

*Built on the Culture Hack Method by [Culture Hack Labs](https://www.culturehack.io/). Part of the CHL AI Agent System. Next: Agent 00 · Q&A.*
