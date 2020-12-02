import random


def check_for_win(players_turn, computers_turn, data):
    global index
    global board
    for q in range(data):
        if (board[q + index] == ['#'] and players_turn) and not computers_turn:
            print("Player wins!")
            return "Player Wins!"
        elif (board[q + index] == ['#'] and computers_turn) and not players_turn:
            print("Computer wins!")
            return "Computer Wins!"
        elif (computers_turn and player_turn) or (not computers_turn and players_turn):
            pass
        board[q + index] = [' ']
    index += data


def user_turn(players_turn, computers_turn):
    # quick Var
    global index
    global board

    # Make sure the user doesnt try to cheese the game
    while True:
        try:
            data = int(input("How many stones would you like to pickup?\n>> "))
            if data > 3 or data < 1:
                raise ValueError
        except ValueError:
            print("Please input an integer value between 1 and 3")
        else:
            break

    print(f"You chose to take {data} stones.")

    check_for_win(players_turn, computers_turn, data)

    print(board)


def algorithm_turn(players_turn, computers_turn):
    # computer vars
    amount_left = 0
    global board
    global index

    # see how many spots are left
    for q in range(len(board)):
        if board[q] == ['X']:
            amount_left += 1

    # "You sly dog, you got me monologuing!"
    print("there are " + str(amount_left + 1) + " stones left.")

    print(f"I choose to take {str((amount_left + 1) % 4)}")

    check_for_win(players_turn, computers_turn, ((amount_left+1) % 4))

    print(board)


while True:
    mode = input("Would you like to go first or choose the amount?\n"
                 " - 'first' or 'f' for First\n"
                 " - 'choose' or 'c' for choosing\n"
                 " - 'rules' or 'r' for rules\n"
                 ">> ")
    if mode == "r" or mode == "rules":
        print("""Here's the basic rules:
        1. Each 'turn' me and you [USER] are going to take turns removing squares from a board, much like this:
        [X] [X] [X] [X] [X] [X] [X] [X] [X] [X] [X] [X]
        after one turn the previous board could look like any one of the following boards:
        [ ] [X] [X] [X] [X] [X] [X] [X] [X] [X] [X] [X]
        [ ] [ ] [X] [X] [X] [X] [X] [X] [X] [X] [X] [X]
        [ ] [ ] [ ] [X] [X] [X] [X] [X] [X] [X] [X] [X]
        if you didn't see, each turn the player who's turn it is will take anywhere from 1 to 3 'stones'
        from the main amount.
        The object of the game is to pick up the last stone
                                                   this one
                                                     ||
                                                     \\/
        [X] [X] [X] [X] [X] [X] [X] [X] [X] [X] [X] [#]  """)

    elif mode == 'f' or mode == 'first':
        # Variables
        index = 0
        board = []
        playing_first = True
        num = 4 * random.randint(2, 5)
        computer_turn = False
        player_turn = True

        # Creating the board
        print(f"I choose a board with {num} stones.")

        for i in range(num - 1):
            board.append(['X'])

        board.append(['#'])

        print(board)

        while playing_first:
            # play Vars
            player_turn = True
            computer_turn = False

            result = user_turn(player_turn, computer_turn)

            # did someone win?
            if result == "Player Wins!":
                break
            elif result == "Computer Wins":
                break

            # computer turn vars
            player_turn = False
            computer_turn = True

            algorithm_turn(player_turn, computer_turn)
