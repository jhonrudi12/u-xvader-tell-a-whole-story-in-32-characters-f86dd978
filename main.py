#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun bounty entry.

Writes a single Wi-Fi network name to /output/entry.txt: the funniest
name that implies a whole story, chosen by scoring a shortlist against
the judge's brief (on-subject joke first, then lands on first read,
then whole story, then fresh, then tight).

Draft pick, revised after a first run: "Ex took the dog. I kept the WiFi"
— the single-sentence draft ("My ex took the dog, not the WiFi") was
only an observation, a relieved aside with no punchline. The two
sentences give the joke a beat: loss, then win. "I kept the WiFi" is
an active victory claim, so the name implies a whole breakup story —
a split, a division of shared things, and a narrator whose priorities
are hilariously skewed toward the router. Dropping "My" tightens it.
"""

import os

# Candidates, scored 0-5 on the judge's criteria in order:
# (on-subject joke, lands on first read, whole story, fresh, tight)
CANDIDATES = {
    "My ex took the dog, not the WiFi": (5, 4, 4, 4, 5),
    "Ex took the dog. I kept the WiFi": (5, 5, 5, 4, 5),
    "He left. I changed the password.": (5, 4, 4, 3, 5),
    "Dad moved out. Password changed.": (5, 3, 4, 3, 5),
    "Divorce finalized. WiFi is mine.": (5, 3, 3, 3, 5),
    "I named it after my ex. Regret.": (5, 3, 3, 4, 4),
    "The WiFi knows what you did": (5, 3, 2, 3, 5),
    "This WiFi is my alibi": (5, 3, 2, 3, 5),
}

# Judge weighs the criteria most important first, so earlier
# criteria count more than later ones.
WEIGHTS = (5, 4, 3, 2, 1)


def score(name: str) -> int:
    """Weighted score of one candidate name."""
    return sum(w * s for w, s in zip(WEIGHTS, CANDIDATES[name]))


def pick_name() -> str:
    """Return the highest-scoring name; ties break to the shorter name."""
    return min(CANDIDATES, key=lambda n: (-score(n), len(n)))


def main() -> None:
    name = pick_name()
    assert 1 <= len(name) <= 32, "entry must be 1-32 characters"
    assert name.strip(), "entry must not be only whitespace"
    assert "\n" not in name, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(name)
    print(name)


if __name__ == "__main__":
    main()
