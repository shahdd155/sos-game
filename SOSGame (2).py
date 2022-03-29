import sys

# Will hold our game board data
_board = [["-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-"]]

    
def display_board():
    print("\n")
    print("     " + " | " + _board[0][0] + " | " + _board[0][1] + " | " + _board[0][2] + " | " + _board[0][3] + " | " + _board[0][
        4] + " | ")
    print("     " + " | " + _board[1][0] + " | " + _board[1][1] + " | " + _board[1][2] + " | " + _board[1][3] + " | " + _board[1][
        4] + " | ")
    print("     " + " | " + _board[2][0] + " | " + _board[2][1] + " | " + _board[2][2] + " | " + _board[2][3] + " | " + _board[2][
        4] + " | ")
    print("     " + " | " + _board[3][0] + " | " + _board[3][1] + " | " + _board[3][2] + " | " + _board[3][3] + " | " + _board[3][
        4] + " | ")
    print("     " + " | " + _board[4][0] + " | " + _board[4][1] + " | " + _board[4][2] + " | " + _board[4][3] + " | " + _board[4][
        4] + " | ")
    print("\n")

#function to get all the possible ways for each player to get a pont when he enters letter s
def get_points_s(row, column):
    points = 0
    # Horizontal
    if _board[row][column: column + 3] == ["S", "O", "S"]:
        points += 1
    if _board[row][column - 2: column + 1] == ["S", "O", "S"]:
        points += 1

    # Vertical
    if row - 2 >= 0:
        if _board[row][column] == "S" and _board[row - 1][column] == "O" and _board[row - 2][column] == "S":
            points += 1
    if row + 2 <= 4:
        if _board[row][column] == "S" and _board[row + 1][column] == "O" and _board[row + 2][column] == "S":
            points += 1

    # Diagonal
    if row - 2 >= 0 and column - 2 >= 0:
        if _board[row - 2][column - 2] == 'S' and _board[row - 1][column - 1] == 'O' and _board[row][column] == 'S':
            points += 1

    if row - 2 >= 0 and column + 2 <= 4:
        if _board[row - 2][column + 2] == 'S' and _board[row - 1][column + 1] == 'O' and _board[row][column] == 'S':
            points += 1

    if row + 2 <= 4 and column - 2 >= 0:
        if _board[row + 2][column - 2] == 'S' and _board[row + 1][column - 1] == 'O' and _board[row][column] == 'S':
            points += 1

    if row + 2 <= 4 and column + 2 <= 4:
        if _board[row + 2][column + 2] == 'S' and _board[row + 1][column + 1] == 'O' and _board[row][column] == 'S':
            points += 1

    return points

#function to get all the possible ways for each player to get a pont when he enters letter O
def get_points_o(row, column):
    points = 0
    # Horizontal
    if _board[row][column - 1: column + 2] == ["S", "O", "S"]:
        points += 1

    # Vertical
    if row - 1 >= 0 and row + 1 <= 4:
        if _board[row - 1][column] == "S" and _board[row][column] == "O" and _board[row + 1][column] == "S":
            points += 1

    # Diagonal
    if column + 1 <= 4 and column - 1 >= 0:
        if row - 1 >= 0 and row + 1 <= 4:
            if _board[row - 1][column - 1] == 'S' and _board[row][column] == 'O' and _board[row + 1][column + 1] == 'S':
                points += 1

        if row - 1 >= 0 and row + 1 <= 4:
            if _board[row - 1][column + 1] == 'S' and _board[row][column] == 'O' and _board[row + 1][column - 1] == 'S':
                points += 1
    return points

def play():
    #to allow each player to enter only  S or O
    let_list = ['S', 'O']
    player_1_points = 0
    player_2_points = 0
    print(" Rules...\n pick a row and a column separated by a comma\n and enter the letter you want to place, either 'S' or 'O'\n"
          " IF you enter an invalid letter or position, your turn is skipped\n Rows and columns start from 0\n")
    display_board()
    player_1_active = True
    player_2_active = False
    while True:
        while player_1_active:
            counter = 0
            for i in _board:
                if '-' not in i:
                    counter += 1
                    if counter == 5:
#at the end of the game if player 2 points is grater than player 1 points so player 2 is the winner
                        if player_2_points > player_1_points:
                            print(" PLAYER TWO WON!")
                            player_1_active = False
                            player_2_active = False
                            break
#at the end of the game if player 1 points is grater than player 2 points so player 1 is the winner
                        elif player_1_points > player_2_points:
                            print(' PLAYER ONE WON!')
                            player_1_active = False
                            player_2_active = False
                            break
#at the end of the game if player 2 points is equal to player 1 points so the game is a draw         
                        elif player_1_points == player_2_points:
                            print(" DRAW!")
                            player_1_active = False
                            player_2_active = False
                            break
            print(" Player ONE's Turn")
            print(f" Player 1's points = {player_1_points}")
            print(f" Player 2's points = {player_2_points}")
            player_1_pos = input(" row, column : ")
            positions = player_1_pos.split(',')
            if len(positions) != 2:
                player_2_active = True
                player_1_active = False
                display_board()
                break
            if not positions[0].isnumeric() or int(positions[0]) > 4 or int(positions[0]) < 0:
                player_2_active = True
                player_1_active = False
                display_board()
                break
            if not positions[1].isnumeric() or int(positions[1]) > 4 or int(positions[1]) < 0:
                player_2_active = True
                player_1_active = False
                display_board()
                break
            player_1_choice = input(" letter : ").upper()
            if len(player_1_choice) >= 2 or player_1_choice not in let_list:
                player_1_choice = '-'
                player_2_active = True
                player_1_active = False
            if _board[int(positions[0])][int(positions[1])] == '-':
                _board[int(positions[0])][int(positions[1])] = player_1_choice
            display_board()
            if get_points_s(int(positions[0]), int(positions[1])):
                player_1_points += get_points_s(int(positions[0]), int(positions[1]))
            elif get_points_o(int(positions[0]), int(positions[1])):
                player_1_points += get_points_o(int(positions[0]), int(positions[1]))
            else:
                player_1_active = False
                player_2_active = True
        while player_2_active:
            counter = 0
            for i in _board:
                if '-' not in i:
                    counter += 1
                    if counter == 5:
                        if player_2_points > player_1_points:
                            print(" PLAYER TWO WON!")
                            player_1_active = False
                            player_2_active = False
                            break
                        elif player_1_points > player_2_points:
                            print(' PLAYER ONE WON!')
                            player_1_active = False
                            player_2_active = False
                            break
                        elif player_1_points == player_2_points:
                            print(" DRAW!")
                            player_1_active = False
                            player_2_active = False
                            break
            print(" Player TWO's Turn")
            print(f" Player 1's points = {player_1_points}")
            print(f" Player 2's points = {player_2_points}")
            player_2_pos = input(" row, column : ")
            positions = player_2_pos.split(',')
            if len(positions) != 2:
                player_1_active = True
                player_2_active = False
                display_board()
                break
            if not positions[0].isnumeric() or int(positions[0]) > 4 or int(positions[0]) < 0:
                player_1_active = True
                player_2_active = False
                display_board()
                break
            if not positions[1].isnumeric() or int(positions[1]) > 4 or int(positions[1]) < 0:
                player_1_active = True
                player_2_active = False
                display_board()
                break
            player_2_choice = input(" letter : ").upper()
            if len(player_2_choice) >= 2 or player_2_choice not in let_list:
                player_2_choice = '-'
                player_2_active = True
                player_1_active = False
            if _board[int(positions[0])][int(positions[1])] == '-':
                _board[int(positions[0])][int(positions[1])] = player_2_choice
            display_board()
            if get_points_s(int(positions[0]), int(positions[1])):
                player_2_points += get_points_s(int(positions[0]), int(positions[1]))
            elif get_points_o(int(positions[0]), int(positions[1])):
                player_2_points += get_points_o(int(positions[0]), int(positions[1]))
            else:
                player_1_active = True
                player_2_active = False


play()
