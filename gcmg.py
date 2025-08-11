#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
gcmg – Git Commit Message Generator (full-body variant)
"""

import subprocess
import sys
from typing import Optional

import click
import ollama

# ------------------------------------------------------------ #
# 1. Gather the staged diff
# ------------------------------------------------------------ #
def get_staged_diff() -> str:
    """Return `git diff --staged` output as a string."""
    try:
        diff = subprocess.check_output(
            ["git", "diff", "--staged"],
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Git failed: {e.output.strip()}", err=True)
        sys.exit(1)

    return diff.strip()

# ------------------------------------------------------------ #
# 2. Ask Ollama to produce a commit message
# ------------------------------------------------------------ #
def generate_commit_message(
    diff: str,
    model: str = "gpt-oss:20b",
    system_prompt: Optional[str] = None,
) -> str:
    """
    Return a Conventional-Commit formatted **full** message
    (Subject, an empty line, then body).
    """
    user_prompt = (
        "以下のコード変更を、**Conventional-Commit 形式の全文**（"
        "Subject 行、空行、Body 行）でまとめてください。\n"
        "Subject 行は `feat: `、`fix: ` などのキーワードで始め、Body は説明文と改行だけで完結させてください。\n\n"
        f"--- 差分 (git diff --staged) ---\n{diff}\n\n"
        "結果は **本文のみ** を返してください。"
    )

    payload = {"model": model, "prompt": user_prompt}
    if system_prompt:
        payload["system"] = system_prompt

    try:
        resp = ollama.generate(**payload)
    except Exception as exc:
        click.echo(f"❌ Ollama で生成失敗: {exc}", err=True)
        sys.exit(1)

    message = resp.get("response", "").strip()
    if not message:
        click.echo("❌ Ollama からメッセージが返ってきませんでした。", err=True)
        sys.exit(1)
    return message

# --------------------------------------------------------- #
# 3. Click CLI
# --------------------------------------------------------- #
@click.command()
@click.option(
    "-m", "--model",
    default="gpt-oss:20b",
    show_default=True,
    help="Ollama model name",
)
@click.option("-s", "--sign-off", is_flag=True, help="Add Signed-off-by")
@click.option(
    "-c", "--commit/--no-commit",
    default=True,
    show_default=True,
    help="Create a new commit after generation",
)
@click.option(
    "-A", "--amend",
    is_flag=True,
    help="Amend the previous commit with the generated message",
)
@click.option(
    "-p", "--system-prompt",
    default=None,
    help="Override the system prompt",
)
def main(model, sign_off, commit, amend, system_prompt):
    """Generate a git commit message from your staged changes."""

    # ------------------------------------------------------------------
    # 1️⃣ Force `commit` off when `--amend` is present
    # ------------------------------------------------------------------
    if amend:
        # Even if the user passed `--commit` or `--no-commit` before,
        # `--amend` takes precedence – we simply reset `commit` to False.
        commit = False
        # If you want to warn the user about an explicit `--commit`,
        # uncomment the next line.
        # click.secho("⚠️  `--commit` is ignored when `--amend` is used.", fg="yellow")

    diff = get_staged_diff()
    if not diff:
        click.echo("⚠️  No staged changes found.")
        # For `--amend`, we *can* proceed even without staged changes
        if not amend:
            sys.exit(0)

    msg = generate_commit_message(diff, model=model, system_prompt=system_prompt)

    click.echo("\n=== Generated commit message ===")
    click.echo(msg)
    click.echo("=== End of generated message ===\n")

    # ------------------------------------------------------------------
    # 2️⃣ Handle the amend case first
    # ------------------------------------------------------------------
    if amend:
        click.confirm("Amend the previous commit with this message?", abort=True)
        cmd = ["git", "commit", "--amend", "-m", msg]
        if sign_off:
            cmd.append("--signoff")
        subprocess.check_call(cmd)
        click.echo("✅ Previous commit amended successfully!")
        return

    # ------------------------------------------------------------------
    # 3️⃣ Normal commit / no-commit
    # ------------------------------------------------------------------
    if commit:
        click.confirm("Do you want to commit with this message?", abort=True)
        cmd = ["git", "commit", "-m", msg]
        if sign_off:
            cmd.append("--signoff")
        subprocess.check_call(cmd)
        click.echo("✅ Commit succeeded!")

if __name__ == "__main__":
    main()