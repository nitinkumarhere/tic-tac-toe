import pickle
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
		print("\n \n")

def check_winner(current_player):
	win_positions = (
		(0, 1, 2),
		(3, 4, 5),
		(6, 7, 8),
		(0, 3, 6),
		(1, 4, 7),
		(2, 5, 8),
		(0, 4, 8),
		(2, 4, 6)
	)
	for combo in win_positions:
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
	try:
		desired = input(f"Enter s to save and exit  \n ******OR***** \nEnter l to load from last saved, \n ******OR***** \nPlayer {current_player}, enter a position (1-9): ")
		print("\n")
		if desired == 's':
			with open("./state.p", 'wb') as f:
				pickle.dump(board, f)
				print("Exiting" )
				break
		if desired == 'l':
			with open("./state.p", 'rb') as f:
				board = pickle.load(f)
				print("Last game is as follows :")
				continue
		else:
			move = int(desired)
		if move < 1 or move > 10:
			print("Invalid position! Please choose a number between 1 and 9.")
			# continue
	except ValueError:
		print("Invalid input! Please enter a number between 1 and 9.")
		continue

	if board[move-1] in [1,2,3,4,5,6,7,8,9]:
		board[move-1] = current_player
	else:
		print("This spot is already taken. Try again.")
		continue

	if check_winner(current_player):
		print_current_board(board)
		print(f"Player {current_player} wins!")
		
		break

	current_player = switch_player(current_player)

#
# p1 = "Player 1, enter your move (0-9): "
# p2 = "Player 2, enter your move (0-9): "
# mp1 = input(p1)
#
# x = board.replace(mp1, "O")
# print(x)
