# gcmg – Git Commit Message Generator  

**gcmg** is a lightweight CLI that reads the diff of your staged files, sends it to an Ollama‑powered large‑language‑model (LLM), and produces a *Conventional‑Commit* style commit message.  If you need, it can also apply that message to the commit or amend the last commit.  

> *Ideal for developers who want instant, AI‑generated commit messages.*

**Repository:** <https://github.com/ryoheikudo/gcmg>  

---

## ✏️  Prerequisites  

- Python
- Ollama
- Git

> **Heads‑up:** The LLM must be reachable – be sure that `ollama serve` is running before launching **gcmg**.

---

## Getting Started

```bash
# 1. Create a folder for the repo (or skip if you cloned)
git clone git@github.com:ryoheikudo/gcmg.git

# 2. Create a virtual‑environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install the package in editable mode
pip install -r requirements.txt
pip install -e .           # installs the console script “gcmg”

# 4. (Optional) Verify the script
gcmg --help
```

---

## 🚀 Running `gcmg` from Any Directory (PATH Setup)

When you run `pip install -e .`, the `gcmg` script is placed in your virtual environment’s `bin` directory (`Scripts` on Windows).
Add that directory to your `PATH` to run `gcmg` from anywhere.

```bash
# Activate the virtual environment
source .venv/bin/activate

# Go to the bin directory and get its full path
cd .venv/bin
VENV_BIN=$(pwd)

# Permanently add it to PATH (Bash/Zsh)
echo "export PATH=\"$VENV_BIN:\$PATH\"" >> ~/.zshrc
source ~/.zshrc
```

Verify:

```bash
cd /any/directory
gcmg --help
```

> 💡 If you activate the virtual environment every time (`source .venv/bin/activate`), you don’t need to change your PATH manually.
 
---

## 📦 Installation as a package  

Installing the package (e.g. with `pip install -e .`) places the console script `gcmg` in the virtual‑environment’s `bin` directory.  Once the environment is activated, you can run `gcmg` without any additional work.

---

## 🚀  Usage

```bash
# 1. Stage the changes you want to commit
git add .

# 2. Dry‑run: see what the commit message will look like
gcmg                     # prints the message and exits

# 3. Commit immediately (creates a new commit)
gcmg --commit             # commits automatically

# 4. Add a *Signed‑off‑by* line
gcmg --sign-off           # includes a Signed‑off‑by header

# 5. Use a different model
gcmg --model gpt-oss:20b

# 6. Amend the most recent commit without adding a new one
gcmg --amend

# 7. Skip committing or amending – just preview
gcmg --no-commit          # same as the default dry‑run
```

Flags can be combined:

```bash
gcmg --amend --sign-off -m gpt-oss:20b
```

### ⚡  Quick‑start  

If you’d only like a preview, simply run `gcmg` without staging any files – the script will abort gracefully, making it safe to use in any repository.

---

## 📜  License  

MIT © 2025  

---

## 👷  Contributing  

Feel free to open issues or submit pull requests – the project is intentionally minimal, and any enhancements are welcome.