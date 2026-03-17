def find_teammates(num_needed):
    print("Finding", num_needed, "teammates...")


def battle_royale():
    # Read number of players
    players = int(input("Enter number of players: "))

    # Full team is 3 players
    teammates_needed = 3 - players

    # Call function to find teammatesd
    if teammates_needed > 0:
        find_teammates(teammates_needed)

    # Start match
    print("Match starting...")


def practice():
    # Read desired map
    desired_map = input("Enter desired map: ")

    # Launch practice
    print("Launching practice on", desired_map)


# Main program
mode = input("Enter game mode: ")

if mode == "br":
    battle_royale()
else:
    practice()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
