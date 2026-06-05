"""
Winning Pitch Skill Example Script

This file demonstrates how the skill resources might be accessed.
It is not required for the skill to function and may be removed.
"""

def generate_pitch_checklist():
    return [
        "Clear problem statement",
        "Compelling solution",
        "Strong demo",
        "Market opportunity",
        "Competitive advantage",
        "Impact metrics",
        "Clear call to action"
    ]


if __name__ == "__main__":
    print("Winning Pitch Checklist")
    print("-" * 30)

    for item in generate_pitch_checklist():
        print(f"✓ {item}")