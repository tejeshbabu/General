'''
Flip the World 
Flip the world is a game. In this game a matrix of size N*M is given, which consists of numbers. Each number can be 1 or 0 only. The rows are numbered from 1 to N, and the columns are numbered from 1 to M.

Following steps can be called as a single move.

Select two integers x,y (1<=x<=N and 1<=y<=M) i.e. one square on the matrix.

All the integers in the rectangle denoted by (1,1) and (x,y) i.e. rectangle having top-left and bottom-right points as (1,1) and (x,y) are toggled(1 is made 0 and 0 is made 1).

For example, in this matrix (N=4 and M=3)

101

110

101

000

if we choose x=3 and y=2, the new state of matrix would be

011

000

011

000

For a given state of matrix, aim of the game is to reduce the matrix to a state where all numbers are 1. What is minimum number of moves required.

INPUT:

First line contains T, the number of testcases. Each testcase consists of two space-seperated integers denoting N,M. Each of the next N lines contains string of size M denoting each row of the matrix. Each element is either 0 or 1.

OUTPUT:

For each testcase, print the minimum required moves.

CONSTRAINTS:

1 <= T <= 30

1 <= N <= 20

1 <= M <= 20

Sample Input (Plaintext Link)
1
5 5
00011
00011
00011
11111
11111

Sample output
1
'''

def interchange(mat,x,y,cnt):
	for i in xrange(1,x+1):
		for j in xrange(0,y+1):
			if(mat[i][j] == 0):
				mat[i][j] = 1
			else:
				mat[i][j] = 0
	cnt += 1
	return [mat,cnt]
	
matrix = {}
n = int(raw_input())
for m in xrange(n):
	count = 0
	r,c = [int(x) for x in raw_input().split()][0:2]
	for i in xrange(1,r+1):
		matrix[i] = list()
		for j in raw_input():
			matrix[i].append(int(j))
	        
	
	for i in xrange(1,r+1):
		for j in xrange(0,c):
			if matrix[r+1-i][c-1-j] == 0:
				matrix_tmp = interchange(matrix,r+1-i,c-1-j,count)
				matrix = matrix_tmp[0]
				count = matrix_tmp[1]
	
	print count
	

