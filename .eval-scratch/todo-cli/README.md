# todo-cli

A tiny todo CLI.

## Usage

```bash
python todo.py add "buy milk"
python todo.py add "urgent fix" -p high
python todo.py list
python todo.py done 1
```

Priorities: `high`, `medium`, `low` (shorthands `h`/`m`/`med`/`l` also work). Tasks without a priority default to `medium`. `list` sorts by priority (high first), then by id.
