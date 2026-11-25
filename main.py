"""One Line of Earned Pride (u-mang-one-line-of-earned-pride-a0138557).

Program/v1 entry: writes the single line to /output/entry.txt
(via MAKEFUN_OUTPUT_DIR). No network, deterministic.
"""

import os

LINE = "On the forty-first morning, Ibu Sari\u2019s stiff hands \u2014 kneading dough before dawn for thirty years \u2014 finally shaped the loaf her late mother made, and her daughter tasted it and went quiet."


def main() -> None:
    # Enforce the competition gate locally: 1-240 chars, one line, non-blank.
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars, gate is 1-240"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
