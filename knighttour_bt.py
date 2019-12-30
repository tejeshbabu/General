#Knights tour

X = [2, 1, -1, -2, -2, -1, 1, 2] 
Y = [1, 2, 2, 1, -1, -2, -2, -1]

def isSafe(b,r,c):
	if (r>-1 and c>-1 and r<N and c<N and b[r][c]==0):
		return True
	else:
		return False

def solveKT(b,step,r,c):
	if step>=N*N:
		return True
	if isSafe(b,r,c):
		step+=1	
		b[r][c] = step
		for i in range(8):
			if solveKT(b,step,r+X[i],c+Y[i]):
				return True		
		b[r][c] = 0
		step -= 1
	return False
	

def showBoard(b):
	for r in b:
		r = [str(x) for x in r]
		print(" ".join(r))

if __name__=='__main__':
	try:
		N=int(input("Enter board size: "))
	except:
		print("Only integers allowed")
	else:
		board = [[0 for x in range(N)] for y in range(N)]
		feasible = solveKT(board,0,0,0)
		if feasible:
			showBoard(board)
		else:
			print("Cannot do a complete tour")
