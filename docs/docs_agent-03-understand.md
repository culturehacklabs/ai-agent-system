# Agent 03 · Understand

*Companion to the "03 — Understand" video. What the Understand agent is, how to work with it, and what goes in and comes out.*

New to the system? Watch the "00 — Introduction" video first, and use Agent 00 for any method question. This guide assumes the agents are already installed.

---

## ✅ Before you start — install checklist (Agent 03 · Understand)

*Uses the same three file types as every agent; only the Agent KBs differ. The three Shared KBs are identical across all agents.*

**Instructions field:**

- [ ] `03_Understand_Instructions.md`

**Agent KBs (upload):**

- [ ] `KB_03_Understand_Module.md`
- [ ] `KB_03_Understand_Actions.md`
- [ ] `KB_03_Understand_Prompting.md`
- [ ] `KB_03_Understand_Tools.md`
- [ ] `KB_03_Understand_MapCheck.md`

**Shared KBs (upload — same in every agent):**

- [ ] `KB_CHL_Method.md`
- [ ] `KB_AI_Fluency.md`
- [ ] `KB_Agent_Directory.md`

*(Agent 03 has a specialised **MapCheck** KB — it powers the single co-creation moment in the phase, the Map Check-in. It loads only at that step.)*

---

## ⬇️ Install it the quick way — the agent zip

Everything in the checklist above also ships as a single **zip** in the repo's [`install v2.0.0`](https://github.com/culturehacklabs/ai-agent-system/tree/main/install%20v2.0.0) folder. Each zip contains two folders that map straight onto the three buckets:

- **`Project Instructions (paste)`** → **bucket 1**. A single text file — open it in any text editor and paste it into the Project's **Instructions** field. *(It's the contents of `03_Understand_Instructions.md`, saved as `.txt` so it opens on any computer without a Markdown viewer.)*
- **`Project Documents (upload)`** → **buckets 2 + 3**. All of Agent 03's KBs *and* the three Shared KBs. Upload every file as Project knowledge.

**Five steps:** (1) download Agent 03's zip; (2) create a new Claude Project named *"CHL Agent 03 — Understand"*; (3) paste the Instructions text into the **Instructions** field; (4) upload everything in `Project Documents (upload)`; (5) start with a prompt from `KB_03_Understand_Prompting.md`.

Prefer to pull the files individually from the repo instead? The checklist above lists every one by name — see the [Install guide](../install.md) for the file-by-file route. The zip is just the fast path; it doesn't replace the repo.

---

## 1. What it is

**Agent 03 · Understand** takes the research package from Agent 02b and turns it into **strategic intelligence about the narrative space**. It applies four analytical tools in sequence — **ANP Analysis** (Attention, Network, Power), **Language Analysis** (frames, metaphors, ideological logic), **Community Mapping** (positioning communities on the Justice/Ontology map), and the **Window of Discourse** (what is mainstream, emerging, or radical, and where the window could shift).

Two ideas to hold onto:

- **Evidence first, interpretation second.** ANP is the evidence-based layer — every claim cites a **Folio ID** from the ANP Source Library. Language Analysis is interpretive — it draws on both the research and your own community knowledge. The order is deliberate.
- **The Ontofake trap.** Some communities perform progressive, plural, or Indigenous-sounding language while their actual practices keep systems of oppression intact — cooptation. Automated analysis is structurally biased toward misreading these as Catalytic or Justice + Onto-shift, because the language looks right. Only practitioner knowledge of actual practice reveals the gap. This is exactly why the Map Check-in exists as a **human co-creation moment**, not an automated output.

Agent 03 surfaces what the analysis points toward. Agent 04 makes the strategic decisions.

---

## 2. General instructions

**Three modes:** Hacking ⚡ (default — moves through the four tools in sequence with a single check-in), Learning 🌱 (write "learning mode" — explains the reasoning behind each tool before proceeding), and **Iteration 🔄** (share your existing community analysis from a prior cycle and it *updates* it with `[Updated]` markers rather than rebuilding).

**How a session flows:** check the **Handoff Checklist** from 02b → confirm the community first drafts (3–5 communities) → run **ANP Analysis** with Folio ID citations → pause for the **Map Check-in** (the one co-creation moment — review and adjust community positioning; the agent explicitly asks whether any upper-right community might really be Ontofake) → run **Language Analysis** → assess the **Window of Discourse** → produce the outputs, ending with **Strategic Insights + Narrative Intentions**.

The Map Check-in offers two pathways: **Lite** (an editable table plus a Mermaid render) or **Visual** (JSON exported to the CHL Narrative Mapper tool and pasted back).

*Starter prompt:* "Here is my Agent 02b package: [paste Narrative Report, ANP Source Library, and completed Handoff Checklist]. Run the full Understand analysis — ANP, map check-in, language analysis, Window of Discourse, and Strategic Insights / Narrative Intentions."

If you get stuck, `KB_03_Understand_Prompting.md` has power prompts for the common situations — going deeper on one community's ANP, jumping straight to the Map Check-in, or requesting more sources from 02b before you proceed.

---

## 3. Input → Output

- **Receives from 02b:** Narrative Report · CSV Database · ANP Source Library (with Folio IDs) · Handoff Checklist. *(Iteration input: your existing community analysis from a prior cycle.)*
- **Produces:** **(A) Community Analysis Report** (profiles + ANP + Language Analysis + Window of Discourse + Strategic Insights + Narrative Intentions in one document) and **(B) Narrative Map** (JSON + Mermaid + summary table).
- **Passes to 04:** the Community Analysis Report + Narrative Map (including the Narrative Intentions and Window of Discourse assessment).

**The handoff in one line:** 02b → Narrative Report + CSV Database + ANP Source Library → **03 → Community Analysis Report + Narrative Map → 04**.

A note on the boundary: Agent 03 produces observations and **Narrative Intentions** (options). Agent 04 turns those into **Narrative Objectives** (decisions). Analysis should not be handed over as strategy.

---

*Built on the Culture Hack Method by [Culture Hack Labs](https://www.culturehack.io/). Part of the CHL AI Agent System. Next: Agent 04 · Recode.*
