SQAURE_SIZE = 3

test_field = [
[1, 0, 0, 9, 0, 4, 0, 8, 2],
[0, 5, 2, 6, 0, 0, 3, 0, 0],
[8, 6, 4, 2, 0, 0, 9, 1, 5],
[0, 1, 0, 0, 4, 9, 8, 0, 6],
[4, 9, 8, 3, 0, 0, 7, 0, 1],
[6, 0, 7, 5, 1, 0, 0, 9, 3],
[0, 8, 6, 0, 3, 5, 2, 0, 9],
[5, 0, 9, 0, 0, 2, 1, 3, 7],
[0, 3, 0, 4, 9, 7, 0, 0, 8]]
# [0, 3, 0, 4],
# [2, 0, 1, 3],
# [4, 0, 0, 1],
# [0, 0, 0, 0]
# ]

def display(field):
	for i in range(len(field)):
		if i % SQAURE_SIZE == 0 and i != 0:
			print('----------------')
		for j in range(len(field)):
			if j % SQAURE_SIZE == 0 and j != 0:
				print('| ',  end='')
			if j == SQAURE_SIZE**2-1:
				print(field[i][j])
			else:
				print(str(field[i][j]), end=' ')

def find_blank(field):
	for i in range(len(field)):
		for j in range(len(field)):
			if field[i][j] == 0:
				return (i, j)
	return None
def check(field, blank_i, blank_j, test_n):
	# check row
	for j in range(len(field)):
		#if true: test_n is valid possibility in row, else: check next num
		if test_n == field[blank_i][j]: return False

	# check colum
	for i in range(len(field)):
		if test_n == field[i][blank_j]: return False

	# check square
	square_x = blank_j // SQAURE_SIZE
	square_y = blank_i // SQAURE_SIZE

	for i in range(square_y*SQAURE_SIZE, (square_y+1)*SQAURE_SIZE):
		for j in range(square_x*SQAURE_SIZE, (square_x+1)*SQAURE_SIZE):
			if field[i][j] == test_n: return False

	return True

def solve(field):
	blanks = find_blank(test_field)

	if not blanks:
		return True
	else:
		i, j = blanks

	for n in range(1, len(field)+1):
		if check(field, i, j, n):
			# add to field
			field[i][j] = n
			if solve(field):
				return True
			
			field[i][j] = 0
	return False

solve(test_field)
display(test_field)




