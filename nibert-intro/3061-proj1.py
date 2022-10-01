
# Python3 Program to decompose
# a matrix into lower and
# upper triangular matrix
MAX = 100
#Find what questions to do
p=7
q=2
r=3
s=7
#A
a=(p%4)+1
b=(q%2)+1
c=(r%2)+1
d=(s%3)+1
import numpy as np 
import matplotlib.pyplot as plt
import math as math
#import scipy
#import scipy.linalg 
#import os

class ludecomp: #passing in n, size of square matrix

	lower = 0 #declaring now bc gonna assign later
	upper = 0
	def __init__(self,n):
		self.lower = [[0 for i in range(n)] for j in range(n)] #creating two class members to be used in lu method
		self.upper = [[0 for i in range(n)] for j in range(n)] #now can call lower and upper in lu in ludecomp class
		
	def lu(self, A, n):
	# Decomposing matrix into Upper
	# and Lower triangular matrix
		for x in range(n):

		# Upper Triangular
			for z in range(x, n):

			# Summation of L(i, j) * U(j, k)
				sum = 0
				for y in range(x):
					sum += (self.lower[x][y] * self.upper[y][z])

			# Evaluating U(i, k)
				self.upper[x][z] = A[x][z] - sum

		# Lower Triangular
			for z in range(x, n):
				if (x == z):
					self.lower[x][x] = 1 # Diagonal as 1
				else:

				# Summation of L(k, j) * U(j, i)
					sum = 0
					for y in range(x):
						sum += (self.lower[z][y] * self.upper[y][x])

				# Evaluating L(k, i)
					self.lower[z][x] = int((A[z][x] - sum) /
									self.upper[x][x])

	# setw is for displaying nicely
		print("Lower Triangular\t\tUpper Triangular")

	# Displaying the result :
		for x in range(n):

		# Lower
			for y in range(n):
				print(self.lower[x][y], end="\t")
			print("", end="\t")

		# Upper
			for y in range(n):
				print(self.upper[x][y], end="\t")
			print("")
A = np.array([[1, 2, 3, 4], [-4, 3, 2, -1], [2, -5, 7, 3], [3, 5, -9, 2]])
B = np.array([p, q, r, s])

matrix = ludecomp(4)
matrix.lu(A, 4)

#now do decomposition math 

Y = np.dot(np.linalg.inv(matrix.lower), B)
X = np.dot(np.linalg.inv(matrix.upper), Y)

print(X)