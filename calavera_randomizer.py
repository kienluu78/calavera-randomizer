"""
Calavera Randomizer Engine v1
-----------------------------
Rolls a Day-of-the-Dead sugar skull from four weighted part categories.
Same seed always gives the same result (deterministic).

Categories: skull shape, colorway, crown, accent.
Weights: higher = more common. Rare parts stay special.

Usage:
    from calavera_randomizer import roll_calavera, describe
    roll = roll_calavera()          # random roll
    roll = roll_calavera(seed=42)   # deterministic roll
    print(describe(roll))
"""

import random

SKULLS = {
    "classic": 40,      # the standard sugar-skull shape
    "round": 25,        # softer, rounder face
    "angular": 20,      # sharp cheekbones, dramatic
    "small": 15,        # petite, childlike proportions
}

COLORS = {
    "white_gold": 30,   # classic white with gold accents
    "magenta_teal": 25, # vivid Day-of-the-Dead palette
    "orange_black": 20, # Halloween-leaning
    "purple_silver": 15,# jewel tones
    "obsidian": 10,     # rare, dark
}

CROWNS = {
    "roses": 30,        # floral crown, most common
    "marigolds": 25,    # cempasuchil
    "hearts": 20,       # love motif
    "stars": 15,        # celestial
    "none": 10,         # bare skull, rare
}

ACCENTS = {
    "heart": 30,
    "butterfly": 25,
    "moon": 20,
    "cross": 15,
    "none": 10,
}


def weighted_choice(options):
    """Pick one key from a {key: weight} dict."""
    total = sum(options.values())
    r = random.uniform(0, total)
    upto = 0
    for key, w in options.items():
        upto += w
        if r <= upto:
            return key
    return list(options.keys())[-1]


def roll_calavera(seed=None):
    """Roll a calavera. Same seed -> same result (deterministic)."""
    if seed is not None:
        random.seed(seed)
    return {
        "skull": weighted_choice(SKULLS),
        "color": weighted_choice(COLORS),
        "crown": weighted_choice(CROWNS),
        "accent": weighted_choice(ACCENTS),
    }


def describe(roll):
    parts = [f"skull={roll['skull']}", f"color={roll['color']}",
             f"crown={roll['crown']}", f"accent={roll['accent']}"]
    return " | ".join(parts)


if __name__ == "__main__":
    # Quick self-test
    r1 = roll_calavera(seed=42)
    r2 = roll_calavera(seed=42)
    assert r1 == r2, "same seed must give same result"
    print("Determinism OK:", describe(r1))
    for i in range(5):
        print(f"Roll {i+1}: {describe(roll_calavera())}")
