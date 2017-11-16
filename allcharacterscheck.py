'''
Checking if all the characters are present in the given string
'''

alphabet = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
n = int(raw_input())

for i in xrange(n):
	string = set(list(raw_input()))
	if(len(string.intersection(alphabet) ) == len(alphabet)):
		print 'YES'
	else:
		print 'NO'
        
	print string.intersection(alphabet)