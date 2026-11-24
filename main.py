"""The One-Line Cat Joke That Lands.

One joke about cats: a single line under 200 characters, with a setup
(a thank-you for a dead mouse) and a turn (the cat now treats gratitude
as a subscription and the human as a tenant behind on rent).
"""

LINE = "My cat brought me a dead mouse, so I thanked him — now he brings me two a day and stares at me like I'm behind on rent."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space, and a single line.
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
