print("""Welcome to Tic Tac Toe!
Player 1: X
Player 2: O
""")

board = [1,2,3,4,5,6,7,8,9]
# with open("./state_game.txt", "r") as f:
#     for line in f:
#         line = line.strip()
#         print(line.format(board=board))

def print_current_board(board):
	with open("game_template.txt", "r") as f:
		for line in f:
			line = line.strip()
			print(line.format(board=board))

def check_winner(current_player):
	win_positions = (
		(1, 2, 3),
		(4, 5, 6),
		(7, 8, 9),
		(1, 4, 7),
		(2, 5, 8),
		(3, 6, 9),
		(1, 5, 9),
		(3, 5, 7)
	)
	for combo in win_positions:
		# print(combo)
		if board[combo[0]] == board[combo[1]] == board[combo[2]] == current_player:
			return True
	else:
		return False


def switch_player(p):
	if p == "X":
		return "O"
	else:
		return "X"

current_player = "X"
while True:

	print_current_board(board)
	try :
		move = int(input(f"Player {current_player}, enter a position (1-9): "))
		if move < 1 or move > 10:
			print("Invalid position! Please choose a number between 1 and 9.")
			# continue
	except ValueError:
		print("Invalid input! Please enter a number between 1 and 9.")
		continue

	if board[move-1] in [1,2,3,4,5,6,7,8,9]:
		# print(board)
		board[move-1] = current_player
	else:
		print("This spot is already taken. Try again.")
		continue

	print(f"{current_player}", check_winner(current_player))
	if check_winner(current_player):
		# print_current_board()
		print(f"Player {current_player} wins!")
		
		break

	current_player = switch_player(current_player)
	print(current_player)

#
# p1 = "Player 1, enter your move (0-9): "
# p2 = "Player 2, enter your move (0-9): "
# mp1 = input(p1)
#
# x = board.replace(mp1, "O")
# print(x)
