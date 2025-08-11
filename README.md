# gcmg – Git Commit Message Generator

**gcmg** is a little‑ish CLI tool that reads the diff of the files you’ve staged, sends it to an 
Ollama‑powered large‑language‑model (LLM) and turns it into a *conventional‑commit* style 
message (and, if you tell it, actually commits it for you).

> *Ideal for developers who want AI‑generated commit messages in one swoop.*

---

## ✏️  Prerequisites

| Item      | How to install                                 |
|-----------|------------------------------------------------|
| **Python 3.9+** | `apt install python3 python3‑venv` (Debian/Ubuntu) |
| **Ollama**      | `curl -fsSL https://ollama.ai/install.sh | sh`<br>`ollama serve`<br>`ollama run gpt‑oss:20b` |
| **Git**         | `apt install git` |

> **Heads‑up:** the LLM itself must be accessible – make sure `ollama serve` is running before 
you launch gcmg.

---

##  Getting Started

```bash
# 1. Fetch the repo (or create a new folder)
mkdir gcmg && cd gcmg
# 2. (If you clone from a Git repo, skip 1.)

# 3. Set up a virtual‑env
python3 -m venv .venv
source .venv/bin/activate

# 4. Install dependencies + console script
pip install -r requirements.txt
pip install -e .           # installs the `gcmg` command

# 5. (Optional) Verify that the script runs
gcmg --help
```

---

## 📦  Installation as a package

If you’ve just built the project locally, the console entry‑point `gcmg` is installed with `pip`.  
Once installed you can drop the `python gcmg.py` trick and just run:

```bash
gcmg --help
```

If you prefer a development install that picks up local changes, use `pip install -e .` instead of the command‑line installs above.

---

## 🚀  Usage

```bash
# 1. Stage any changes you want to commit
git add .

# 2. Dry‑run: just show what the commit message would look like
gcmg                         # ← prints the message and exits

# 3. Commit immediately (adds a new commit)
gcmg --commit                # ← commits automatically

# 4. Add a Signed‑off‑by line
gcmg --sign-off              # ← includes a Signed‑off‑by header

# 5. Use a different model
gcmg --model gpt‑oss:20b

# 6. Amend the most recent commit without creating a new one
gcmg --amend

# 7. Skip committing or amending – just preview
gcmg --no-commit             # same as the default dry‑run
```

You can combine flags:

```bash
gcmg --amend --sign-off -m gpt‑oss:20b
```

### ⚡️  Quick‑start

*If you only wish to preview, run `gcmg` without staging any files – the script will abort gracefully, so you can use it safely in any repository.*

---

## 📜  License

MIT © 2025

---

## 👷  Contributing

Feel free to open issues or pull requests – the project is intentionally minimal, and any enhancements are very welcome.