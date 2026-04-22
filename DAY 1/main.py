#Band Name generator BY ME
import random


ADJECTIVES = [
    "Electric",
    "Neon",
    "Silent",
    "Golden",
    "Midnight",
    "Cosmic",
    "Velvet",
    "Broken",
    "Wild",
    "Crimson",
    "Silver",
    "Burning",
    "Lonely",
    "Restless",
    "Thunder",
]

NOUNS = [
    "Wolves",
    "Echo",
    "Saints",
    "Riot",
    "Dreamers",
    "Monsters",
    "Satellites",
    "Hearts",
    "Mirage",
    "Storm",
    "Rebels",
    "Shadows",
    "Pilots",
    "Ghosts",
    "Comets",
]

STYLES = [
    "rock",
    "metal",
    "indie",
    "punk",
    "pop",
    "jazz",
    "electronic",
]


def make_band_name():
    return f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)}"


def style_reaction(style):
    reactions = {
        "rock": "That sounds arena-ready.",
        "metal": "That name could headline a thunderstorm.",
        "indie": "That feels cool enough for a basement gig.",
        "punk": "That name wants to break the rules already.",
        "pop": "That sounds catchy and chart-friendly.",
        "jazz": "That has a smooth late-night club vibe.",
        "electronic": "That sounds ready for lasers and synths.",
    }
    return reactions.get(style, "That band has potential.")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please type yes or no.")


def play_round(round_number):
    print(f"\nRound {round_number}")
    print("-" * 24)
    style = random.choice(STYLES)
    print(f"Your band's style is: {style.upper()}")
    input("Press Enter to generate a band name...")

    band_name = make_band_name()
    print(f"\nYour generated band name is: {band_name}")
    print(style_reaction(style))

    like_name = ask_yes_no("Do you want to keep this name? (yes/no): ")
    if like_name:
        print("Nice choice. Your fans approve.")
        return 1

    reroll = ask_yes_no("Want to reroll for a new band name? (yes/no): ")
    if reroll:
        new_name = make_band_name()
        print(f"\nSecond chance name: {new_name}")
        print("Fresh name, fresh energy.")
        return 1 if ask_yes_no("Keep the reroll? (yes/no): ") else 0

    print("No worries. Some legendary bands need time.")
    return 0


def main():
    print("Welcome to Band Name Blast!")
    print("Generate wild band names and build your score.")

    player_name = input("\nWhat should I call you? ").strip() or "Player"
    score = 0
    round_number = 1

    while True:
        score += play_round(round_number)
        print(f"\n{player_name}, your current score is: {score}")

        if not ask_yes_no("\nPlay another round? (yes/no): "):
            break
        round_number += 1

    print("\nGame over.")
    print(f"Final score: {score}")
    print("Thanks for playing Band Name Blast!")


if __name__ == "__main__":
    main()
