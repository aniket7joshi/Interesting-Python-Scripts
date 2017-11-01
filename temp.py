#!/usr/bin/python3

import unittest
from matrix import Matrix

class MatrixTest(unittest.TestCase):
	def test_add1(self):
		m1 = Matrix([[1, 2], [3, 4]], 2, 2)
		m2 = Matrix([[5, 6], [7, 8]], 2, 2)
		self.assertEqual(str(m1 + m2), str(Matrix([[6, 8], [10, 12]], 2, 2)))

	def test_add2(self):
		m1 = Matrix([[1, 2, 3], [3, 4, 5]], 2, 3)
		m2 = Matrix([[5, 6], [7, 8]], 2, 2)
		with self.assertRaises(AssertionError):
			m1 + m2

	def test_sub1(self):
		m1 = Matrix([[1, 2], [3, 4]], 2, 2)
		m2 = Matrix([[5, 6], [7, 8]], 2, 2)
		self.assertEqual(str(m1 - m2), str(Matrix([[-4, -4], [-4, -4]], 2, 2)))

	def test_mul1(self):
		m1 = Matrix([[1, 2], [3, 4], [8, 9]], 3, 2)
		m2 = Matrix([[5, 6, 7], [7, 8, 3]], 2, 3)
		self.assertEqual(str(m1 * m2), str(Matrix([[19, 22, 13],
												   [43, 50, 33],
												   [103, 120, 83]], 3, 3)))
		
	def test_mul2(self):
		m1 = Matrix([[5, 6, 7], [7, 8, 3]], 2, 3)
		m2 = Matrix([[1, 2], [3, 4]], 2, 2)
		with self.assertRaises(AssertionError):
			m1 * m2
class MatrixIteratorTest(unittest.TestCase):
	def test_it1(self):
		m1 = Matrix([[1, 2], [3, 4]], 2, 2)
		self.assertEqual(list(m1), [1, 2, 3, 4])

	def test_it2(self):
		m1 = Matrix([[5, 6, 7], [7, 8, 3]], 2, 3)
		self.assertEqual(list(m1), [5, 6, 7, 7, 8, 3])



if __name__ == '__main__':

	unittest.main()
