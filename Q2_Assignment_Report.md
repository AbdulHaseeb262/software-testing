# Assignment 2 – Question 2 Report

Repository: https://github.com/AbdulHaseeb262/software-testing

## Objective
Create a public GitHub repository, add a README, upload a triangle classification program (any language), show local commits, and explain how bugs are reported and debugging is applied.

## Steps Followed
1) GitHub account and repository
- Sign up at GitHub if needed.
- Create public repository named, for example, `software-testing`.
- Add a README to describe the project.

2) Upload code file (triangle classification)
- Option A (Web): Open repo → Add file → Upload files → upload `triangle.py` → Commit changes.
- Option B (Local + Git):
  - Create local folder and add your files.
  - Initialize Git and commit.
  - Connect remote and push.

3) Local directory and commit demonstration
- Commands:
```
mkdir software-testing
cd software-testing
# Place triangle.py and README.md into this folder

git init
git add triangle.py README.md
git commit -m "Add triangle classification program and README"
# Connect the repo you created on GitHub
# Replace <your-username> properly

git remote add origin https://github.com/<your-username>/software-testing.git
git branch -M main
git push -u origin main

# Make an edit (e.g., add validation) and commit again
git add triangle.py
git commit -m "Add triangle inequality validation"
# See recent commits
git log -n 3
```

## Triangle Classification Code (Python)
```
import math

EPS = 1e-9

def classify_triangle(a: float, b: float, c: float):
    # Sort so that c is the largest side
    sides = sorted([a, b, c])
    a, b, c = sides

    # Basic validation
    if a <= 0 or b <= 0 or c <= 0:
        return {
            "valid": False,
            "reason": "Sides must be positive.",
        }
    if a + b <= c + EPS:
        return {
            "valid": False,
            "reason": "Triangle inequality violated (a + b must be > c).",
        }

    # Side-based classification
    if abs(a - b) < EPS and abs(b - c) < EPS:
        sides_type = "Equilateral"
    elif abs(a - b) < EPS or abs(b - c) < EPS or abs(a - c) < EPS:
        sides_type = "Isosceles"
    else:
        sides_type = "Scalene"

    # Angle-based classification using the largest side (c)
    a2b2 = a * a + b * b
    c2 = c * c
    diff = a2b2 - c2
    if abs(diff) < EPS:
        angle_type = "Right"
    elif diff > 0:
        angle_type = "Acute"
    else:
        angle_type = "Obtuse"

    # Primary classification per assignment wording
    if angle_type == "Acute":
        primary = "Acute"
    elif sides_type == "Isosceles":
        primary = "Isosceles"
    else:
        primary = "Scalene"

    return {
        "valid": True,
        "sides_type": sides_type,
        "angle_type": angle_type,
        "primary": primary,
        "sides_sorted": (a, b, c),
        "a2b2": a2b2,
        "c2": c2,
    }


def main():
    print("Enter three side lengths of a triangle (e.g., 3 4 5):")
    try:
        parts = input().strip().split()
        if len(parts) != 3:
            print("Please enter exactly three values.")
            return
        a, b, c = map(float, parts)
    except Exception:
        print("Invalid input. Please enter numeric values.")
        return

    result = classify_triangle(a, b, c)

    if not result["valid"]:
        print("Not a valid triangle:", result["reason"])
        return

    print(f"Sides (sorted): {result['sides_sorted']}")
    print(f"By sides: {result['sides_type']}")
    print(f"By angles: {result['angle_type']}")
    print(f"Primary classification: {result['primary']}")

    # Debugging info
    print(f"a^2 + b^2 = {result['a2b2']:.6f}")
    print(f"c^2 = {result['c2']:.6f}")


if __name__ == "__main__":
    main()
```

## How Bugs Are Reported on GitHub (Issues)
- Open repo → Issues tab → New issue.
- Include:
  - Title (short summary)
  - Description: steps to reproduce, expected vs actual, environment (OS, Python version), and screenshots.
- Example bug:
  - Title: "Near-right triangles misclassified due to floating-point equality"
  - Steps: Input `3 4 5.0000001`
  - Expected: Right (or tolerance handled)
  - Actual: Obtuse
  - Fix approach: use epsilon tolerance when comparing squares.

## Apply Debugging
- Use IDE debugger (e.g., VS Code):
  - Set breakpoints in `classify_triangle`.
  - Watch expressions: `sides_sorted`, `a2b2`, `c2`, `diff`.
  - Step Over branches to confirm the code path.
- Validate with test values:
  - `(3, 4, 5)` → Right, scalene
  - `(2, 2, 2)` → Equilateral, acute
  - `(2, 2, 3)` → Isosceles, acute
  - `(3, 4, 6)` → Not a valid triangle

## Screenshots to Include (in Word)
- Repo home page showing it is Public.
- README displayed in the repo.
- Commit history (`git log` or GitHub commits tab).
- New Issue creation page with bug details and labels.

## Conclusion
- The repository is set up, code is uploaded, commits are demonstrated, and a clear bug reporting and debugging workflow is documented.