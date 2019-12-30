# nQueens Problem

def isSafe(b,r,c):
	N=len(b)
	for y in range(c,-1,-1):
		if(b[r][y]==1):
			return False
	for x,y in zip(range(r,-1,-1),range(c,-1,-1)):
		if(b[x][y]==1):
			return False
	for x,y in zip(range(r,N),range(c,-1,-1)):
		if(b[x][y]==1):
			return False
	return True
	

def solveNQ(b,col):
	N=len(b)
	if col>=N:
		return True
	for i in range(N):
		if isSafe(b,i,col):
			b[i][col] = 1
			if solveNQ(b,col+1):
				return True
			b[i][col] = 0
	return False

def showBoard(b):
	for r in b:
		r = ["Q" if x==1 else "-" for x in r ]
		print(" ".join(r))

if __name__ == "__main__":
	try:
		N = int(input("Enter size of board: "))
	except:
		print("Only integers")
	else:
		board = [[0 for x in range(N)] for x in range(N)]
		feasible = solveNQ(board,0)
		if feasible:
			showBoard(board)
		else:
			print("No solution")


