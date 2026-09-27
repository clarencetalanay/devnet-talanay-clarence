# Module 1 — Git & GitHub

**Student:** [Clarence Nathan Lee D. Talanay]
**Date:** [9/27/2026]

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[Git is like an undo button for an entire project. Whenever a code is working, you save a snapshot to go back to. If you try something new later and break everything, Git lets you instantly jump back in time to when it worked. GitHub is the website where those prjects are stored and shared online, making it easy to back up your work and collaborate with others from anywhere in the world.]

---

## Key vocabulary (in your own words)

- repository: It is the master folder for projects. It contains all project files and the complete history of every change ever made.

- commit: A checkpoint. Whenever finishing code and want to make a savepoint, you make a commit to capture a snapshot of your work along with a short note explaining what you changed.

- branch: An isolated workspace. It lets you experiment with a new features or fix bugs safely without breaking the main working version of your code.

- push / pull: Uploading and downloading. Push sends your local checkpoints up to GitHub, and pull downloads the latest updates from GitHub down to your computer.

- pull request: It is a request to combine your branch's work into the main project. It gives your team a chance to review your code, chat about it, and test it before it becomes the final output.

- merge conflict: A disagreement that happens when two people has changed the exact same line of code in different ways.

---

## Walking through what I did

[For a real workflow. I'll create a feature branch called update-readme. After finishing a code I'll make a checkpoint using git commit, then uploaded it to Github with git push, and then I'll open a pull request on github to merge those changes into the main project.]

```
# paste your actual commands here
```
git checkout -b update-readme
git add README.md / git add .
git commit -m "Update README"
git push origin update-readme

---

## A mistake I made (or one I want to avoid)

[A mistake to avoid is committing untested, half-finished code directly to the main branch instead of always double-checking your current workspace with git status and working inside a separate feature branch.]

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
