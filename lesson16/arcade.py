import guess_number
import rps
import sys

def arcade(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def choose_game():
        nonlocal name

        playerchoice = input(
            f'\n{name}, welcome to the arcade!\n\nPlease chooce a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press "x" to exit the Arcade')

        if playerchoice not in ["1", "2", "x"]:
            print(f"{name}, please enter 1, 2, or x.")
            return choose_game()

        player = int(playerchoice)

        if (player == 1):
            return rps(name)
        elif (player == 2):
            return guess_number(name)
        else:
            print("See you next time!\n")
            sys.exit(f"Bye, {name}! 👋🏼")

    return choose_game


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    arcade = arcade(args.name)
    arcade()
