# Triangle Classification Program

This program reads three side lengths and classifies the triangle by sides (equilateral, isosceles, scalene) and by angles (acute, right, obtuse). A "primary" classification is also printed to match the assignment wording (acute, scalene, isosceles).

## How to Run
- Prerequisite: Python 3.8+
- Command:
  - `python triangle.py`
  - Enter three values when prompted (e.g., `3 4 5`).

## Sample
Input: `3 4 5`
- By sides: Scalene
- By angles: Right
- Primary classification: Scalene (angle is Right, but the assignment’s requested categories are acute/scalene/isosceles)

## Debugging Tips
- Set a breakpoint inside `classify_triangle`.
- Inspect `sides_sorted`, `a2b2` vs `c2`, and branching conditions.
- Use Step Over to follow the classification logic.

## Git Quick Start
Initialize and commit:
- `git init`
- `git add triangle.py README.md`
- `git commit -m "Add triangle classification program and README"`

Connect to GitHub and push:
- `git remote add origin https://github.com/<your-username>/triangle-classifier.git`
- `git branch -M main`
- `git push -u origin main`

## Known Considerations
- Floating-point equality is handled with a small tolerance, which improves right-triangle detection for values like `5.0000001`.