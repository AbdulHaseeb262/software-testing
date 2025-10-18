Assignment 2 – Q2 GitHub Repository and Debugging Guide

Goal
- Create a GitHub account and public repository, add a README, and upload a triangle classification program. Show local commits, and explain bug reporting and debugging workflow.

Part A: Create GitHub Account and Repository (Web)
- Visit https://github.com and sign up (use your academic email if you want student benefits).
- After sign-in, click the "+" icon → New repository.
- Repository name: triangle-classifier (example).
- Visibility: Public.
- Initialize with a README: Checked.
- Click Create repository.

Part B: Upload Code (Two Options)
Option 1 – Direct upload in web UI
- Open your repo → Add file → Upload files → Drag and drop triangle.py → Commit changes.

Option 2 – Push from local machine (recommended)
- Create local project folder and initialize git:
  - mkdir triangle-classifier
  - cd triangle-classifier
  - Copy triangle.py and README.md into this folder.
  - git init
  - git add triangle.py README.md
  - git commit -m "Add triangle classification program and README"
- Connect local repo to GitHub:
  - On GitHub repo page → Click Code → copy HTTPS URL (e.g., https://github.com/<your-username>/triangle-classifier.git)
  - git remote add origin https://github.com/<your-username>/triangle-classifier.git
  - git branch -M main
  - git push -u origin main

Part C: Check Changes with git commit
- Make a change (e.g., add input validation in triangle.py):
  - Edit triangle.py
  - git add triangle.py
  - git commit -m "Add triangle inequality validation"
  - git log -n 3 (shows last 3 commits)

Part D: Bug Reporting in GitHub (Issues)
- Open your repo → Issues tab → New issue.
- Provide a clear title and description:
  - Title: "Near-right triangles misclassified due to floating-point equality"
  - Description:
    - Steps to reproduce: Input sides 3, 4, 5.0000001
    - Expected: Classified as Right (or tolerance considered)
    - Actual: Classified as Obtuse
    - Environment: Python 3.10, Windows 11
    - Attachments: Screenshot of output
- Labels: bug, enhancement (optional).
- Submit issue.

Part E: Apply Debugging to the Triangle Program
- Set breakpoints in your IDE (VS Code → Run and Debug → Python).
- Useful watch expressions:
  - sorted sides (a ≤ b ≤ c)
  - a*a + b*b (sum of squares)
  - c*c (largest side squared)
  - difference = abs((a*a + b*b) - (c*c))
- Use Step Over on classification branches to confirm which path is taken.
- If dealing with floats, avoid exact equality; use an epsilon tolerance.
- Write unit tests or quick checks:
  - (3, 4, 5) → Right, scalene
  - (2, 2, 2) → Equilateral, acute
  - (2, 2, 3) → Isosceles, acute
  - (3, 4, 6) → Not a valid triangle

Part F: Close the Bug via a Pull Request
- Create a branch to fix the bug:
  - git checkout -b fix/float-tolerance
  - Implement tolerance for equality comparisons (see code provided in triangle.py).
  - git add triangle.py
  - git commit -m "Use epsilon tolerance for right-triangle check"
  - git push -u origin fix/float-tolerance
- Open a Pull Request on GitHub:
  - Compare fix/float-tolerance → main
  - Link the issue by typing "Fixes #<issue-number>" in the PR description.
  - Review and merge.

Notes
- Keep commits small and focused.
- Always write descriptive commit messages.
- Use Issues for bugs, Discussions for questions, and Wiki for documentation.