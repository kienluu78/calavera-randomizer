# Calavera Randomizer Engine v1

Rolls a Day-of-the-Dead sugar skull from four weighted part categories.
Same seed always gives the same result (deterministic).

## Categories

| Category | Options (weight) |
|----------|------------------|
| Skull | classic (40), round (25), angular (20), small (15) |
| Color | white_gold (30), magenta_teal (25), orange_black (20), purple_silver (15), obsidian (10) |
| Crown | roses (30), marigolds (25), hearts (20), stars (15), none (10) |
| Accent | heart (30), butterfly (25), moon (20), cross (15), none (10) |

## Usage

```python
from calavera_randomizer import roll_calavera, describe

roll = roll_calavera()          # random roll
roll = roll_calavera(seed=42)   # deterministic roll
print(describe(roll))
```

## Design notes

- **Weighted randomness**: common parts show up most, rare ones stay special.
- **Deterministic**: same seed = same calavera, so a kid can re-roll the exact same one.
- **Parts are data**: swap in real assets later without touching the logic.
- **No uploads**: curated parts library only, nothing user-generated.

## Integration

Built for the FaceMesh app. The engine returns a dict of four part keys;
the app maps those to actual assets (images, colors, overlays).

## Tests

- Determinism: same seed gives same result.
- Distribution over 1000 rolls matches the weights.
