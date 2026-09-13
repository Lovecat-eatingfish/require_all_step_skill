#!/usr/bin/env python3
"""A tiny todo CLI."""
import json, sys, os
from pathlib import Path

STORE = Path(os.environ.get("TODO_STORE", Path.home() / ".todo_cli.json"))

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
PRIORITY_ALIASES = {"h": "high", "hi": "high", "m": "medium", "med": "medium", "l": "low"}
DEFAULT_PRIORITY = "medium"

def load():
    if STORE.exists():
        return json.loads(STORE.read_text(encoding="utf-8"))
    return []

def save(items):
    STORE.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")

def normalize_priority(raw):
    p = raw.strip().lower()
    p = PRIORITY_ALIASES.get(p, p)
    if p not in PRIORITY_ORDER:
        print(f"todo: invalid priority '{raw}' (use high/medium/low)")
        sys.exit(1)
    return p

def add(args):
    text_parts = []
    priority = DEFAULT_PRIORITY
    i = 0
    while i < len(args):
        if args[i] in ("-p", "--priority"):
            if i + 1 >= len(args):
                print("todo: --priority requires a value (high/medium/low)")
                sys.exit(1)
            priority = normalize_priority(args[i + 1])
            i += 2
        else:
            text_parts.append(args[i])
            i += 1
    if not text_parts:
        print("todo: usage: add [-p high|medium|low] <text>")
        sys.exit(1)
    items = load()
    items.append({"id": len(items) + 1, "text": " ".join(text_parts), "priority": priority, "done": False})
    save(items)
    print(f"todo: added #{len(items)} ({priority})")

def list_items():
    items = load()
    if not items:
        print("todo: no items")
        return
    items.sort(key=lambda it: (PRIORITY_ORDER.get(it.get("priority", DEFAULT_PRIORITY), 1), it["id"]))
    for it in items:
        mark = "x" if it["done"] else " "
        print(f"[{mark}] #{it['id']} [{it.get('priority', DEFAULT_PRIORITY)}] {it['text']}")

def done(item_id):
    items = load()
    for it in items:
        if it["id"] == item_id:
            it["done"] = True
    save(items)
    print(f"todo: #{item_id} done")

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "add":
        add(sys.argv[2:])
    elif cmd == "done":
        done(int(sys.argv[2]))
    else:
        list_items()

if __name__ == "__main__":
    main()
