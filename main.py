print("""Welcome to Tic Tac Toe!
Player 1: X
Player 2: O
""")


with open("./game_state.txt", "r") as f:
	status =str( f.read())
	print(status)



p1 = "Player 1, enter your move (0-9): "
p2 = "Player 2, enter your move (0-9): "
mp1 = input(p1)

x = status.replace(mp1, "O")
print(x)
