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

    # A primary classification aligned with assignment wording
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

    # Debugging info (useful when stepping through)
    print(f"a^2 + b^2 = {result['a2b2']:.6f}")
    print(f"c^2 = {result['c2']:.6f}")


if __name__ == "__main__":
    main()