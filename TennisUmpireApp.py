import random

# Players
player_1 = ""
player_2 = ""

# Points, games, sets lists
points_list = [0, 15, 30, 40]
games_list = [0, 1, 2, 3, 4, 5, 6]
sets_list = [0, 1, 2]
tiebrake_list = [0, 1, 2, 3, 4, 5, 6, 7]
supertiebreak_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Current server (for rotation)
current_server = ""

def program_start():
    global player_1, player_2
    print("===================================")
    print("Welcome to the Amateur Tennis Match Tool!")
    print("===================================")
    player_1 = input("Enter name of Player 1: ")
    player_2 = input("Enter name of Player 2: ")
    print(f"Great! {player_1} vs {player_2}!\nLet's start the match!\n")

def coin():
    global current_server
    print("Flipping a coin to decide who serves first...")
    current_server = random.choice([player_1, player_2])
    print(f"{current_server} will serve first!\n")

def rotate_server():
    global current_server
    current_server = player_1 if current_server == player_2 else player_2

def display_score(p1_points, p2_points, p1_games, p2_games, p1_sets, p2_sets, stage="Points"):
    print("-" * 50)
    if stage == "Points":
        print(f"Points  | {player_1}: {points_list[p1_points]} - {player_2}: {points_list[p2_points]}")
    print(f"Games   | {player_1}: {p1_games} - {player_2}: {p2_games}")
    print(f"Sets    | {player_1}: {p1_sets} - {player_2}: {p2_sets}")
    print("-" * 50 + "\n")

def game(p1_games, p2_games, p1_sets, p2_sets):
    p1_points = 0
    p2_points = 0
    while True:
        winner = input(f"Who won the point? {player_1}/{player_2}: ")
        if winner == player_1:
            p1_points += 1
        elif winner == player_2:
            p2_points += 1
        else:
            print("Please type a valid player name!")
            continue

        display_score(min(p1_points, 3), min(p2_points, 3), p1_games, p2_games, p1_sets, p2_sets, stage="Points")

        if p1_points >= 4:
            print(f"Game won by {player_1}!\n")
            rotate_server()
            return player_1
        elif p2_points >= 4:
            print(f"Game won by {player_2}!\n")
            rotate_server()
            return player_2

def tiebrake():
    p1_points = 0
    p2_points = 0
    while True:
        winner = input(f"Who won the tie-break point? {player_1}/{player_2}: ")
        if winner == player_1:
            p1_points += 1
        elif winner == player_2:
            p2_points += 1
        else:
            print("Please type a valid player name!")
            continue
        print("-" * 50)
        print(f"Tie-break | {player_1}: {p1_points} - {player_2}: {p2_points}")
        print("-" * 50 + "\n")
        if p1_points >= 7 and (p1_points - p2_points) >= 2:
            print(f"Set won by {player_1} via tie-break!")
            return player_1
        elif p2_points >= 7 and (p2_points - p1_points) >= 2:
            print(f"Set won by {player_2} via tie-break!")
            return player_2

def supertiebrake():
    p1_points = 0
    p2_points = 0
    while True:
        winner = input(f"Who won the super tie-break point? {player_1}/{player_2}: ")
        if winner == player_1:
            p1_points += 1
        elif winner == player_2:
            p2_points += 1
        else:
            print("Please type a valid player name!")
            continue
        print("-" * 50)
        print(f"Super tie-break | {player_1}: {p1_points} - {player_2}: {p2_points}")
        print("-" * 50 + "\n")
        if p1_points >= 10 and (p1_points - p2_points) >= 2:
            print(f"Match won by {player_1} via super tie-break!")
            return player_1
        elif p2_points >= 10 and (p2_points - p1_points) >= 2:
            print(f"Match won by {player_2} via super tie-break!")
            return player_2

def set(p1_sets, p2_sets):
    p1_games = 0
    p2_games = 0
    while True:
        winner = game(p1_games, p2_games, p1_sets, p2_sets)
        if winner == player_1:
            p1_games += 1
        else:
            p2_games += 1

        display_score(0,0,p1_games,p2_games,p1_sets,p2_sets, stage="Games")

        if p1_games == 6 and p2_games == 6:
            print("Tie-break!")
            return tiebrake()
        elif p1_games >= 6 and (p1_games - p2_games) >= 2:
            print(f"Set won by {player_1}!\n")
            return player_1
        elif p2_games >= 6 and (p2_games - p1_games) >= 2:
            print(f"Set won by {player_2}!\n")
            return player_2

def match():
    p1_sets = 0
    p2_sets = 0
    while True:
        winner = set(p1_sets, p2_sets)
        if winner == player_1:
            p1_sets += 1
        else:
            p2_sets += 1

        display_score(0,0,0,0,p1_sets,p2_sets, stage="Sets")

        if p1_sets == 1 and p2_sets == 1:
            print("Super tie-break to decide the match!")
            winner = supertiebrake()
            print(f"Congratulations {winner}! You won the match!")
            break
        elif p1_sets >= 2:
            print(f"Congratulations {player_1}! You won the match!")
            break
        elif p2_sets >= 2:
            print(f"Congratulations {player_2}! You won the match!")
            break

# Run program
program_start()
coin()
match()

