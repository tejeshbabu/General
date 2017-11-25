#!/usr/bin/python
'''
Given N separate integer points on the Cartesian plane satisfying: there is no any three of them sharing a same X-coordinate. 
Your task is to count the number of rectangles (whose edges parrallel to the axes) created from any four of given points.

Input

There are several test cases (ten at most), each formed as follows:
The first line contains a positive integer N (N ≤ 105).
N lines follow, each containing a pair of integers (each having an absolute value of 109 at most) describing 
coordinates of a given point.
The input is ended with N = 0.
Output

For each test case, output on a line an integer which is the respective number of rectangles found.
Example

Input:
6
7 1
3 5
3 1
1 5
1 1
7 5
0

Output:
3
'''

from itertools import izip as zip, count

def num_coords():
	no_coords = input("Enter number of coordinates:")
	if no_coords < 4:
		print "\nAtleast give 4 coords to make a polygon\n"
		no_coords = num_coords()
	return no_coords

def get_coords(num):
	i = 0
	coord_x = []
	coord_y = []
	while i < num:
		i = i+1
		x,y = [int(x) for x in raw_input("Enter two numbers here: ").split()]
		if coord_x.count(x) == 2:
			print 'Choose any other x coordinate.'
			i=i-1
		else:
			coord_x.append(x)
			coord_y.append(y)
	return [coord_x,coord_y]

def indices_X(listX,x):
	return [i for i, j in zip(count(), listX) if j == x]

def indices_Y(listY,y):
	return [i for i, j in zip(count(), listY) if j == y]

def values_X(listX,listInd):
	outList = []
	for ind in listInd:
		outList.append(listX[ind])
	return outList

def values_Y(listY,listInd):
	outList = []
	for ind in listInd:
		outList.append(listY[ind])
	return outList


def setRectcoords(listRect):
	rectSet = []
	for coords in listRect:
		for i in range(len(coords[0])):
			for j in coords[0][i+1:]:
				r =  (coords[0][i],j)
				rectSet.append((r,tuple(coords[1])))
	rectSet = list(set(rectSet))
	return rectSet

coords_num = num_coords()
coords_raw = get_coords(coords_num)
distinctX  = list(set(coords_raw[0]))
coords_rect = []

for x in distinctX:
	if coords_raw[0].count(x) == 2:
		x_ind = indices_X(coords_raw[0],x)
		y_ind = {}
		x_val = {}
		y_val = values_Y(coords_raw[1],x_ind)
		for y in y_val:
			y_ind[y] = indices_Y(coords_raw[1],y)
		for y,yi in y_ind.items():
			x_val[y] = values_X(coords_raw[0],yi)

		Xcoords_rect = []
		Ycoords_rect = []
		for y,x in x_val.items():
			Xcoords_rect.append(x)
			Ycoords_rect.append(y)
		Xcoords_rect = 	list(set(Xcoords_rect[0]).intersection(set(Xcoords_rect[1])))
		coords_rect.append([Xcoords_rect,Ycoords_rect])

		result = coords_rect
	else:
		result =  0

if result != 0:
	rect_coords = setRectcoords(result)
	print '\n\n',len(rect_coords),' Rectangles can be formed'
else:
	print '\n\nNo Rectangles can be formed'
