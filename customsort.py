#!/usr/bin/python
'''

You have a set of numbers. a1, a2, a3, a4.....an.
numbers are random and may repeat.

Arrange the number in order such that x1 > x2 < x3 > x4 < x5 > x6.......

x1 has no relation ship with x3, x4, x5...
x2 has no relation ship with x4, x5...
x3 has no relation ship with x1, x5, x6...
and so on.


There maybe many feasible solution to this problem see that the final answer reaches any one of them.
If the input is like 22,22,22 then it should output a message as no feasible solution but for an input 
like this 7  7  7 3 3 it should print out a solution like : 7 3 7 3 7.

'''

class customSort():
	values = []
	values_cSorted = []
	feasibility = True
	def __init__(self, size):
		for i in range(size):
			val = input("Enter a number:")		#constructor function
			self.values.append(val)
		# print "\n\n"+','.join(str(elem) for elem in self.values)
		self.values.sort()
		self.sorting()

	def sorting(self,vals = values,cSorted = values_cSorted,feasible = feasibility):
		size = len(vals)/2
		lower_vals = vals[0:size]
		higher_vals = vals[size:]
		print vals.count(lower_vals[size-1]),size
		if (vals.count(lower_vals[size-1]) > size ):
			feasible = False
		if feasible:
			for i in range(size):
				cSorted.append(higher_vals[i])
				cSorted.append(lower_vals[i])
			if len(lower_vals) != len(higher_vals):
				cSorted.append(higher_vals[size])
		self.output(feasible = feasible)

	def output(self,cSorted = values_cSorted,feasible = feasibility):
		if feasible:
			char = " > "
			result = ""
			for i in cSorted:
				result = result+str(i)+char
				if char == " > ":
					char = " < "
				elif char == " < ":
					char = " > "
			print "\n\nResult: "+result[:len(result)-len(char)]+"\n\n"

		else:
			print "No feasible sorting possible as required"
			

mySorter = customSort(input("\nHow many integers do you want to sort? "))
