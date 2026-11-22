#!/usr/bin/env python3
"""Write the entry text for 'The Red Scarf on the Fence Post'.

Stdlib only, no network. Writes the entry to /output/entry.txt
(or $OUTPUT_DIR/entry.txt when set, for local testing).
"""

import os

ENTRY = (
    "Each winter my sister ties her red scarf to the fence post at our "
    "lane's end, so I can find home in the snow. Last November the post "
    "was bare. I waited past dark, then tied my own coat there. In the "
    "morning the scarf was back, knotted tight around my coat, holding me."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    data = ENTRY.encode("utf-8")
    print(f"wrote {path}: {len(data)} bytes, {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
