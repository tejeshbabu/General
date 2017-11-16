from random import randint
from collections import Counter 
import string

chars = string.lowercase#+string.digits


D = input("How many characters yow wanna play with?\n")
N = ""
for m in xrange(D):
	N = N + chars[randint(0,len(chars)-1)]
n = [x for x in str(N)]
g = None
gn=0
CURSOR_UP = '\033[F'
ERASE_LINE = '\033[K'
# print N
print("Start entering your guesses")
while g!=N:
	gn = gn+1
	g = raw_input("Guess "+str(gn)+": ")
	if(len(g)!=len(N)):
		print (CURSOR_UP + ERASE_LINE+"Guess#"+str(gn)+ " : "+ g + " - "+"It contains only "+str(D)+" digits")
		continue
	b,c = 0,0
	b = sum([i==j for i,j in zip(N,g)])
	c = abs(b - sum((Counter(N) & Counter(g)).values()))
	if(len(N)==b):
		print (CURSOR_UP + ERASE_LINE+"You have taken "+str(gn)+" guess"+("es" if gn>1 else "")+" to find this secret number : "+N)
		break
	print(CURSOR_UP + ERASE_LINE+"Guess#"+str(gn)+ " : "+ g + " - "+ str(b)+ " Bulls & "+str(c)+ " Cows")
	
