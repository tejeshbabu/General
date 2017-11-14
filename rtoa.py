romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def convert_rtoa(r):
	if r in romans:
		return int(romans[r])
	else:
		l = []
		v = 0
		i = 0
		for x in r:
			l.append(x)
		while i < len(l)-1:
			if(romans[l[i+1]]>romans[l[i]]):
				v += convert_rtoa(l[i+1]) - convert_rtoa(l[i])
				i = i+1
			else:
				v = v + convert_rtoa(l[i])
				if(i==len(l)-2):
					v = v + convert_rtoa(l[i+1])
			i = i+1
		return v
