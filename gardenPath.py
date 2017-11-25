#!/usr/bin/python

from copy import deepcopy
garden = list()

#Garden formation
size = int(raw_input("Enter the size of garden:"))
startx,starty = [int(k) for k in raw_input("Enter X Y coordinates(separated by space) of Garden entrance point: ").split()][:2]
start = [startx,starty]
for x in xrange(size):
	garden.append([1]*size)

for x in xrange(size*size):
	inf = [int(k) for k in raw_input("Enter X Y coordinates(separated by space) of infected plants(Give -1 at end): ").split()][:2]
	if (inf[0] == -1) :
		break;
	else:
		garden[inf[0]][inf[1]] = 0

#Printing Garden
for x in garden:
	for y in x:
		print y,
	print '\n',

#Finding infections

infections = list()
for x in xrange(len(garden)):
	for y in xrange(len(garden[x])):
		if garden[x][y] == 0:
			infections.append([x,y])

print "Infections: ",infections

#Traversing through infections
path = [start]
minD = 0
#inf = deepcopy(infections)
while len(infections)>0:
	startd = list()
	for x in infections:
		startx = abs(x[0] - start[0])
		starty = abs(x[1] - start[1])
		startd.append(startx + starty)

	a = infections[startd.index(min(startd))]
	infections.pop(startd.index(min(startd)))
	start = deepcopy(a)
	path.append(start)
	minD = minD + min(startd)

#Show path

show_path = path[0]
for i in xrange(1,len(path)):
	show_path = str(show_path)+"-->"+str(path[i])
print "Path: ",show_path
print "Total Distance: ",minD



