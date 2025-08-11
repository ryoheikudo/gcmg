# gcmg – Git Commit Message Generator

**gcmg** is a tiny CLI that reads your staged diff, asks an Ollama-powered
LM to turn it into a conventional-commit style message, and (optionally) commits it for you.

> *Built for developers who want instant, AI-enhanced commit messages.*

---

## ✏️  Prerequisites

| Item | How to install |
|------|----------------|
| **Python 3.9+** | `apt install python3 python3-venv`  (Debian/Ubuntu) |
| **Ollama** | `curl -fsSL https://ollama.ai/install.sh | sh`  <br>Then start the server: `ollama serve`  <br>Once the server is running, pull a model – e.g. `ollama run gpt-oss:20b` |
| **Git** | `apt install git` |

---

## 🔧  Getting Started

```bash
# 1. Fetch the repo (or create a new folder)
mkdir gcmg && cd gcmg
# 2. (If you clone from a Git repo, skip 1.)

# 3. Create virtual-env
python3 -m venv .venv
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. (Optional) Verify that the script runs
python gcmg.py --help
```

### Usage

```bash
# 1. Stage some changes
git add .

# 2. Run the generator
python gcmg.py               # ← Shows the generated message
python gcmg.py --commit       # ← Commits automatically
python gcmg.py --sign-off     # ← Adds Signed-off-by line
python gcmg.py -m gpt-oss:20b      # ← Specify another model
```

> **Tip**  
> The script aborts if you haven’t staged any changes, so you can safely run it without `git 
add` if you only want a dry-run.

---

## 📜  License

MIT © 2025

---

## 👷  Contributing

Feel free to open issues or pull requests – the project is intentionally minimal, and any 
enhancements are welcome.