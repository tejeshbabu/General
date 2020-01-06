#Sudoku Solver

from copy import deepcopy
import math

def printSudoku(s):
	c = 0

	vline = "+—----"*len(s)+"+"
	for x in s:
		c += 1
		if(c in [1,4,7]):
			print("#====="*len(s)+"#")
		else:
			print("#"+vline[1:18]+"#"+vline[19:36]+"#"+vline[37:-1]+"#")
		line0 = "‖  "+"  |  ".join(" " for y in x)+"  ‖"
		line = "‖  "+"  |  ".join(str(y) if y>0 else " " for y in x)+"  ‖"
		print(line0[:18]+"‖"+line0[19:36]+"‖"+line0[37:])
		print(line[:18]+"‖"+line[19:36]+"‖"+line[37:])
		print(line0[:18]+"‖"+line0[19:36]+"‖"+line0[37:])
	print("#====="*len(s)+"#")


def makeSudoku(size):
	# sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9] ]

	# sudoku = [[0,8,0,7,0,0,0,9,0], [5,0,0,4,0,0,0,2,0], [2,0,9,0,3,0,7,0,0], [0,1,0,0,0,4,0,0,0], [0,6,5,1,0,9,4,8,0], [0,0,0,2,0,0,0,6,0], [0,0,8,0,1,0,6,0,5], [0,3,0,0,0,2,0,0,8], [0,5,0,0,0,6,0,7,0] ]

	# sudoku = [[4, 1, 3, 0, 0, 0, 5, 0, 0], [0, 0, 0, 0, 3, 0, 0, 4, 0], [7, 0, 0, 4, 0, 0, 0, 0, 0], [1, 0, 4, 2, 0, 0, 3, 8, 0], [0, 0, 0, 7, 0, 0, 0, 1, 5], [0, 5, 9, 0, 8, 3, 0, 0, 2], [0, 4, 0, 0, 0, 2, 1, 3, 0], [9, 0, 0, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 4, 7, 0, 6, 9] ]

	# sudoku = [[0, 0, 7, 2, 0, 5, 0, 0, 0], [0, 5, 0, 0, 4, 0, 0, 0, 3], [4, 0, 2, 0, 7, 0, 8, 0, 5], [0, 9, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 8, 0, 0, 0, 6], [5, 0, 0, 9, 1, 3, 0, 0, 0], [0, 0, 6, 0, 0, 8, 1, 5, 0], [8, 0, 5, 0, 0, 1, 2, 0, 0], [3, 0, 0, 0, 0, 0, 0, 8, 4]]

	# # unsolved
	# sudoku = [[0, 8, 0, 0, 7, 5, 6, 0, 0], [0, 9, 0, 0, 0, 0, 1, 0, 0], [7, 0, 4, 0, 1, 0, 0, 5, 0], [0, 4, 2, 0, 0, 0, 7, 0, 0], [1, 0, 0, 0, 4, 0, 8, 3, 0], [0, 0, 0, 1, 2, 3, 5, 0, 6], [8, 0, 0, 0, 0, 1, 0, 0, 0], [4, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 3, 8, 4, 0, 7]]

	# sudoku = [[1, 4, 0, 0, 0, 3, 0, 8, 6], [6, 8, 0, 4, 0, 0, 7, 3, 0], [0, 2, 0, 5, 6, 8, 1, 4, 0], [4, 0, 0, 0, 0, 0, 2, 5, 0], [0, 9, 0, 2, 7, 4, 8, 6, 0], [0, 0, 0, 0, 0, 6, 0, 9, 0], [9, 5, 6, 1, 0, 2, 0, 0, 0], [0, 3, 4, 0, 9, 0, 6, 1, 5], [7, 1, 0, 6, 0, 0, 9, 2, 0]]

	# sudoku = [[0, 5, 0, 0, 6, 0, 1, 3, 0], [0, 0, 9, 5, 7, 0, 4, 2, 0], [4, 6, 1, 9, 0, 0, 0, 0, 8], [2, 9, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 4, 0, 0, 0, 0], [6, 8, 0, 3, 0, 0, 0, 0, 2], [0, 7, 0, 0, 0, 2, 0, 1, 0], [5, 0, 0, 0, 9, 7, 0, 6, 0], [0, 0, 0, 0, 8, 0, 0, 0, 0]]

	# sudoku = [[0, 0, 2, 0, 0, 0, 0, 1, 3], [0, 3, 0, 5, 0, 0, 6, 0, 4], [0, 0, 0, 3, 8, 2, 0, 9, 0], [0, 2, 0, 1, 6, 0, 4, 0, 0], [1, 0, 3, 0, 7, 9, 0, 0, 0], [0, 0, 0, 8, 0, 3, 0, 0, 9], [0, 7, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 7, 0, 8, 0], [0, 9, 0, 2, 0, 8, 5, 0, 0]]


	# sudoku = [[4, 0, 0, 0, 5, 6, 2, 0, 0], [0, 0, 0, 3, 0, 8, 0, 5, 0], [0, 0, 0, 0, 0, 1, 3, 0, 7], [0, 0, 0, 2, 6, 5, 0, 0, 9], [6, 2, 0, 0, 4, 3, 0, 0, 5], [0, 0, 5, 0, 0, 0, 6, 4, 2], [0, 0, 0, 0, 0, 0, 5, 0, 4], [8, 5, 0, 0, 7, 0, 0, 0, 0], [3, 0, 4, 5, 0, 9, 8, 0, 0]]
	# Custom Inputs
	sudoku = [[0 for x in range(size)] for x in range(size)]

	for x in range(size):
		i = [int(y) for y in input("Enter row "+ str(x+1) + " numbers (csv format): ").split(",")[:size]]
		for y in range(len(i)):
			sudoku[x][y] = i[y]

	return sudoku

def getNoElemsFilled(sudoku):
	sudoLen = len(sudoku)
	count = 0
	for r in range(sudoLen):
		for c in range(sudoLen):
			if sudoku[r][c]!=0:
				count += 1
	return count

def getSudokuSum(sudoku):
	res = 0
	for x in sudoku:
		res += sum(x)
	return res

def getPossibleSum(possibles):
	res = 0
	for x in possibles:
		for y in x:
			res += sum(y)
	return res

def getCompleteSum(size):
	return int(size*size*(size+1)*0.5)

def getCubeXY(row,col,combine=True):
	cx = (row//3)+1
	cy = (col//3)+1
	if combine:
		return str(cx)+str(cy)
	else:
		return (cx,cy)

def getRowElements(sudoku,row):
	return list((set(sudoku[row]) - set([0])))

def getColElements(sudoku,col):
	cols = []
	for r in range(len(sudoku)): 
		cols.append(sudoku[r][col])
	return list((set(cols) - set([0])))

def getCubeElems(sudoku,r=None,c=None):
	cubes = range(int(math.sqrt(len(sudoku))))
	result = {}

	if r == None or c == None:
		cx = cy = list(map(lambda a:a*3,cubes))
	else:
		cx,cy = getCubeXY(r,c,False)
		cx = [(cx-1)*3]
		cy = [(cy-1)*3]

	for xc in cx:
		for yc in cy:
			cubeXY = getCubeXY(xc,yc)
			result[cubeXY] = []
			for x in cubes:
				row = x+xc
				for y in cubes:
					col = y+yc
					result[cubeXY].append(sudoku[row][col])
	return result


def getRule1(sudoku,possibles):
	sudoLen = len(sudoku)
	for r in range(sudoLen):
		row_elems = getRowElements(sudoku,r)
		for x in row_elems:
			for c in possibles[r]:
				if x in c:
					c.remove(x)

		for c in range(sudoLen):
			if sudoku[r][c] != 0:
				possibles[r][c] = []
			else:
				col_elems = getColElements(sudoku,c)
				for y in col_elems:
					if y in possibles[r][c]:
						possibles[r][c].remove(y)

				cube_elems = getCubeElems(sudoku,r,c)
				cube_no = getCubeXY(r,c)
				for z in cube_elems[cube_no]:
					if z in possibles[r][c]:
						possibles[r][c].remove(z)
	return possibles

def getRule2(sudoku,possibles):
	sudoLen = len(sudoku)
	cubes = range(int(math.sqrt(sudoLen)))
	for r in range(sudoLen):
		for c in range(sudoLen):
			if sudoku[r][c]==0:
				temp = set(deepcopy(possibles[r][c]))
				cx,cy = getCubeXY(r,c,False)
				cX = (cx-1)*3
				cY = (cy-1)*3
				for i in cubes:
					x = cX + i
					for j in cubes:
						y = cY + j
						if(x!=r or y!=c):
							temp = temp - set(possibles[x][y])
							# print(r,c,":",x,y,":",possibles[r][c],possibles[x][y])
				if(len(temp) == 1):
					possibles[r][c] = list(temp)

	return possibles

def populate(sudoku,possibles,itemsFilled):
	sudoLen = len(sudoku)
	for r in range(sudoLen):
		for c in range(sudoLen):
			if(len(possibles[r][c])==1 and sudoku[r][c]==0):
				sudoku[r][c] = possibles[r][c][0]
				itemsFilled += 1
	return sudoku,possibles,itemsFilled



if __name__ == '__main__':
	sudoku_size = int(input("Enter size of sudoku: "))
	# sudoku_size = 9
	q = makeSudoku(sudoku_size)
	print("\r\n")

	possibles = [[[x for x in range(1,sudoku_size+1)] for x in range(sudoku_size)] for x in range(sudoku_size)]

	b4Filling = -1
	itemsFilled = getNoElemsFilled(q)
	using_dp = False
	dp_counter = 0 
	dp_counter_max = 0
	dp_counter_xy = [0,0]
	while(getSudokuSum(q) != getCompleteSum(sudoku_size) and itemsFilled<(sudoku_size*sudoku_size) and b4Filling!=itemsFilled):
		possibles = getRule1(q,possibles)
		b4Filling = deepcopy(itemsFilled)
		q,possibles,itemsFilled = populate(q,possibles,itemsFilled)

		possibles = getRule2(q,possibles)
		q,possibles,itemsFilled = populate(q,possibles,itemsFilled)
		if b4Filling==itemsFilled:
			if(not using_dp):
				for x in range(sudoku_size):
					for y in range(sudoku_size):
						if len(possibles[x][y]):
							dp_counter_max = len(possibles[x][y])
							dp_counter_xy = [x,y]
							break
					if(dp_counter_max > 0):
						break
				q_temp = deepcopy(q)
				possibles_temp = deepcopy(possibles)
				itemsFilled_temp = deepcopy(itemsFilled)
			else:
				q = deepcopy(q_temp)
				possibles = deepcopy(possibles_temp)
				itemsFilled = deepcopy(itemsFilled_temp)
			using_dp = True

			if dp_counter >= dp_counter_max:
				print("No Solution")
			else:
				dp_possible = possibles[dp_counter_xy[0]][dp_counter_xy[1]]
				dp_possible.remove(dp_possible[dp_counter])
				dp_counter += 1
				q,possibles,itemsFilled = populate(q,possibles,itemsFilled)


	printSudoku(q)

	