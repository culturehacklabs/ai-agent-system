#!/usr/bin/env python3
"""Build the per-agent install zips from agents/.

Each zip contains:
  <ID>/Project Instructions (paste)/<ID>_Instructions.txt
  <ID>/Project Documents (upload)/  ← the agent's KB_*.md files + shared KBs

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


def documents(agent_dir):
    docs = sorted(agent_dir.glob("KB_*.md")) + SHARED
    if agent_dir.name == "00_QA":
        docs += sorted(AGENTS.glob("*/KB_*_Module.md"))
    # de-duplicate by name, keep order
    seen, out = set(), []
    for d in docs:
        if d.name not in seen:
            seen.add(d.name)
            out.append(d)
    return out


def build(agent_dir, out_dir):
    aid = agent_dir.name
    zpath = out_dir / f"{aid}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(agent_dir / f"{aid}_Instructions.md",
                f"{aid}/Project Instructions (paste)/{aid}_Instructions.txt")
        for d in documents(agent_dir):
            z.write(d, f"{aid}/Project Documents (upload)/{d.name}")
    return zpath


def main():
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "install v2.1.0"
    out_dir.mkdir(parents=True, exist_ok=True)
    for agent_dir in sorted(p for p in AGENTS.iterdir() if p.is_dir() and p.name != "shared"):
        print(build(agent_dir, out_dir).relative_to(ROOT) if out_dir.is_relative_to(ROOT) else build(agent_dir, out_dir))


if __name__ == "__main__":
    main()
