"""Example usage for Douglas-Peucker Trajectory Simplification Skill."""
from client import DouglasPeucker

def main():
    print("Executing Douglas-Peucker Simplification...")
    raw_path = [(0.0, 0.0), (1.0, 0.1), (2.0, -0.1), (3.0, 5.0), (4.0, 0.0), (5.0, 0.0)]
    simplified = DouglasPeucker.simplify(raw_path, epsilon=2.0)
    print(f"Original: {len(raw_path)} points, Simplified: {len(simplified)} points: {simplified}")
    assert len(simplified) == 3, f"Expected 3 points, got {len(simplified)}"
    print("Douglas-Peucker Simplification verified successfully!")

if __name__ == "__main__":
    main()
