#!/usr/bin/env python3
"""Build the per-agent install zips from agents/.

Standard zip (<out>/<ID>.zip), for Claude Projects and paid ChatGPT plans:
  <ID>/Project Instructions (paste)/<ID>_Instructions.txt
  <ID>/Project Documents (upload)/  ← the agent's KB_*.md files + shared KBs

ChatGPT Free bundle (<out>/chatgpt-free/<ID>_ChatGPT_Free.zip), for plans
that allow only 5 files per Project. Same Instructions, but the KBs are
merged into at most 5 files. Each original file starts with a
"# FILE: <name>" heading so the agent can still find it by name:
  1_<ID>_Core.md            ← Module + Actions KBs
  2_<ID>_Other_KBs.md       ← the agent's remaining KBs
  3_<ID>_Phase_Modules.md   ← Agent 00 only: every phase Module KB
  N_Shared_KBs.md           ← the three shared KBs (numbered last)

Agent 00 (Q&A) also bundles every phase Module KB, since it answers
questions about all phases.

Usage: python3 scripts/build_install_zips.py [output_dir]
"""
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENTS = ROOT / "agents"
SHARED = sorted((AGENTS / "shared").glob("KB_*.md"))
FREE_PLAN_MAX_FILES = 5


def phase_modules(agent_dir):
    if agent_dir.name != "00_QA":
        return []
    return [m for m in sorted(AGENTS.glob("*/KB_*_Module.md")) if m.parent != agent_dir]


def documents(agent_dir):
    return sorted(agent_dir.glob("KB_*.md")) + SHARED + phase_modules(agent_dir)


def merged_groups(agent_dir):
    """(file name, [source KBs]) for the ChatGPT Free bundle, skipping empty groups."""
    aid = agent_dir.name
    own = sorted(agent_dir.glob("KB_*.md"))
    core = [f for f in own if f.stem.endswith("_Module") or "_Actions" in f.stem]
    rest = [f for f in own if f not in core]
    groups = [
        (f"{aid}_Core.md", core),
        (f"{aid}_Other_KBs.md", rest),
        (f"{aid}_Phase_Modules.md", phase_modules(agent_dir)),
        ("Shared_KBs.md", SHARED),
    ]
    groups = [(f"{i}_{name}", files) for i, (name, files) in enumerate((g for g in groups if g[1]), 1)]
    assert len(groups) <= FREE_PLAN_MAX_FILES, f"{aid}: {len(groups)} merged files"
    return groups


def merge(files):
    return "\n\n".join(f"# FILE: {f.name}\n\n{f.read_text(encoding='utf-8').strip()}\n" for f in files)


def instructions(agent_dir):
    return agent_dir / f"{agent_dir.name}_Instructions.md"


def build(agent_dir, out_dir):
    aid = agent_dir.name
    zpath = out_dir / f"{aid}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(instructions(agent_dir), f"{aid}/Project Instructions (paste)/{aid}_Instructions.txt")
        for d in documents(agent_dir):
            z.write(d, f"{aid}/Project Documents (upload)/{d.name}")
    return zpath


def build_chatgpt_free(agent_dir, out_dir):
    aid = agent_dir.name
    zpath = out_dir / f"{aid}_ChatGPT_Free.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(instructions(agent_dir), f"{aid}/Project Instructions (paste)/{aid}_Instructions.txt")
        for name, files in merged_groups(agent_dir):
            z.writestr(f"{aid}/Project Files (upload)/{name}", merge(files))
    return zpath


def main():
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "install v2.1.0"
    free_dir = out_dir / "chatgpt-free"
    free_dir.mkdir(parents=True, exist_ok=True)
    for agent_dir in sorted(p for p in AGENTS.iterdir() if p.is_dir() and p.name != "shared"):
        for zpath in (build(agent_dir, out_dir), build_chatgpt_free(agent_dir, free_dir)):
            print(zpath.relative_to(ROOT) if zpath.is_relative_to(ROOT) else zpath)


if __name__ == "__main__":
    main()
