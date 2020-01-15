def display_board(board):

	print('\n'*100)
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('----')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('----')
	print(board[1] + '|' + board[2] + '|' + board[3])

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
print(display_board(test_board))
print(display_board(test_board))

def player_input():

	marker = ''

	while marker != 'X' or marker != 'O':
		marker = raw_input("Player 1, choose X or O: ").upper()

	if marker == 'X':
		return ('X', 'O')
	else: 
		return ('O', 'X')



player1_marker, player2_marker = player_input()
print(player_input())