import random 
def display_board(board):

	print('\n'*100)
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('----')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('----')
	print(board[1] + '|' + board[2] + '|' + board[3])

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
print(display_board(test_board))


def player_input():

	marker = ''

	while not (marker == 'X' or marker == 'O'):
		marker = input("Player 1: Choose X or O: ").upper()

	if marker == 'X':

		return ('X', 'O')
	else: 
		return ('O', 'X')

def place_marker(board, marker, position):
	board[position] = marker

print(place_marker(test_board,'$', 8))
print(display_board(test_board))



def win_check(board, mark):
	   return ((board[7] ==  board[8] ==  board[9] == mark) or # across the top
    (board[4] ==  board[5] ==  board[6] == mark) or # across the middle
    (board[1] ==  board[2] ==  board[3] == mark) or # across the bottom
    (board[7] ==  board[4] ==  board[1] == mark) or # down the middle
    (board[8] ==  board[5] ==  board[2] == mark) or # down the middle
    (board[9] ==  board[6] ==  board[3] == mark) or # down the right side
    (board[7] ==  board[5] ==  board[3] == mark) or # diagonal
    (board[9] ==  board[5] ==  board[1] == mark)) # diagonal


def choose_first():

	flip = random.randint(0,1)

	if flip ==0:
		return 'Player 1'
	else:
		return 'Player 2'


def space_check(board, position):
	return board[position] == ""

def full_board_check(board):

	for i in range(1,10):
		if space_check(board, i):
			return False
	# Board is full if we return true	
	return True


def player_choice(board):

	position = 0

	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
		position = int(input('Choose a position: (1-9) '))

	return position


















