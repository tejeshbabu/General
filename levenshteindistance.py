'''
Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other
'''

def printMatrix(mat):
	c=0
	for x in mat:
		c = len(x)
		print("-"+"----"*c)
		print("| "+" | ".join( str(i) for i in x ) + " |")
	print("-"+"----"*c)


def getLevenshteinDistance(str1,str2):
	max_col = len(str1)+2
	max_row = len(str2)+2
	levenshteinMatrix = [[0 for x in range(max_col)] for y in range(max_row)]
	levenshteinMatrix[0][0] = " "
	levenshteinMatrix[1][0] = " "
	levenshteinMatrix[0][1] = " "
	for c in range(max_col-2):
		levenshteinMatrix[0][c+2] = str1[c]
	for r in range(max_row-2):
		levenshteinMatrix[r+2][0] = str2[r]

	for c in range(max_col-1):
		levenshteinMatrix[1][c+1] = c
	for r in range(max_row-1):
		levenshteinMatrix[r+1][1] = r


	for r in range(2,max_row):
		for c in range(2,max_col):
			levenshteinMatrix[r][c] = min(
											levenshteinMatrix[r][c-1] + 1,
											levenshteinMatrix[r-1][c] + 1,
											levenshteinMatrix[r-1][c-1] + (0 if levenshteinMatrix[0][c] == levenshteinMatrix[r][0] else 1),
										)


	return levenshteinMatrix,levenshteinMatrix[max_row-1][max_col-1]


if __name__ == "__main__":
	str1 = input("Enter String 1: ")
	str2 = input("Enter String 2: ")
	ldM,ld  = getLevenshteinDistance(str1,str2)
	printMatrix(ldM)
	print("\n")
	print("Levenshtein Distance for changing from "+str1+" to "+ str2+ " is "+ str(ld) )
	print("\n")

