#!/usr/bin/python3

class Matrix:
	'''Class for matrix operations'''

	def __init__(self, lofl, m, n):
		'''Initializes the matrix.

		lofl: List of lists
		m: Number of rows in the matrix
		n: Number of columns in the matrix
		'''

		assert len(lofl) == m
		for row in lofl:
			assert len(row) == n

		self.lofl = lofl
		self.m = m
		self.n = n
		self.index=-1

	def __add__(self, mat):
		assert self.m == mat.m
		assert self.n == mat.n
		# Write similar assertions in other methods

		# Your code here
		a = self.lofl
		m = self.m
		n = self.n
		b = mat.lofl
		c = []
		for i in range(m):
			temp = []
			for j in range(n):
				temp.append(a[i][j] + b[i][j])
			c.append(temp)

		return Matrix(c, m, n)

	def __sub__(self, mat):
		assert self.m == mat.m
		assert self.n == mat.n
		
	# 	# Your code here
		a = self.lofl
		m = self.m
		n = self.n
		b = mat.lofl
		c = []
		for i in range(m):
			temp = []
			for j in range(n):
				temp.append(a[i][j] - b[i][j])
			c.append(temp)

		return Matrix(c, m, n)

	def __mul__(self, mat):
		assert self.n == mat.m
	
	# 	# Your code here
		a=self.lofl
		b=mat.lofl
		m=self.m
		n=self.n
		p=mat.n
		c=[]
		for i in range(m):
			temp2=[]
			for j in range(p):
				sum=0
				for k in range(n):
					sum=sum+(a[i][k]*b[k][j])
				temp2.append(sum)
			c.append(temp2)	
		
		return Matrix(c,m,p)			

	



	def __str__(self):
		stri = ''
		for i, row in enumerate(self.lofl):
			for j, elem in enumerate(row):
				stri += str(elem) + ' '
			stri += '\n'

		return stri

	def __next__(self):
		if self.index is self.n * self.m -1:
			self.index = -1
			raise StopIteration
		self.index += 1
		return self.lofl[int(self.index / self.n)][int(self.index % self.n)]

	def __iter__(self):	
		return self	