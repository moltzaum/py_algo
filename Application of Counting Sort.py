'''
Describe an algorithm that, given n integers in the range 0 to k, preprocesses its input
and then answers any query about how many of the n integers fall into a range [a..b] in
O(1) time.

Your algorithm should use Θ(n + k) preprocessing time.

You can use data structures similarly as in Counting-Sort.
Consider the array C after it stores the prefix sums.
It helps to understand the very concept of “prefix sums”:
Suppose we have a sequence of numbers a = (a0, a1, . . . , an).
Then a sequence (p0, p1, . . . , pn) is the sequence of prefix sums of the sequence a when
for k = 0, 1, ..., n
'''

#A is the input
#B is the sorted output
#range of numbers in A is from [0, k] inclusive
def countingSort(A, B, k):
	C = [0]*(k+1)
	# Basic Count
	for i in range(0, len(A)):
		C[A[i]] += 1
	# Prefix Summation
	for i in range(1, k+1):
		C[i] += C[i-1]
	# Load into B
	for i in range(len(A)-1, -1, -1):
		val = A[i]
		pos = C[val]
		B[pos-1] = val
		C[val] -= 1

def countingSortTest():
	#A = [2, 5, 3, 0, 2, 3, 0, 3]
	A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
	B = [0]*len(A)
	k = max(A)
	print(A)
	countingSort(A, B, k)
	print(B)

# A is the input
# k is the maximum of A
# a and b is the interval we want to check
def findMaxInRange(A, k, a, b):
	if (a > b): return
	C = [0]*(k+1)
	# Basic Count
	for i in range(0, len(A)):
		C[A[i]] += 1
	# Prefix Summation
	for i in range(1, k+1):
		C[i] += C[i-1]
	print('[' + str(a) + ' ' + str(b), end = ']--> ')
	
	# A = [0, 0, 2, 2, 3, 3, 3, 5]	(input)
	# C = [2, 2, 4, 7, 7, 8]		(prefix sum)
	# a = 2, b = 5					(bounds)
	# C[a] = 4, C[b] = 8
	# C[a] is the count of numbers less than or equal to a
	# C[b] is the count of numbers less than or equal to b
	# 
	# There are 4 numbers in A less than or equal to 2
	# There are 8 numbers in A less than or equal to 5
	# C[b] - C[a] is bounded from (a, b]
	# 8 - 4 -> 4
	# There are 4 numbers in the bounds (2, 5]
	# 
	# We want the range from [2, 5], so we can
	# just look in the range (2-1, 5]. The only
	# problem with this is that this is out of 
	# bounds for a == 0. To fix this though, we
	# only need to print out C[b] because it goes
	# from [0, b] by itself.
	
	if (a != 0): print(C[b] - C[a-1])
	else: print(C[b])
	
def myAlgorithmTest():
	A = [2, 5, 3, 0, 2, 3, 0, 3]
	#A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
	B = [0]*len(A)
	k = max(A)
	print([1, 2, 3, 4, 5, 6, 7, 8], '(indexes)')
	print(A, '(array)')
	print('\n[a b]--> n, where n is the number of items in range [a, b]')
	findMaxInRange(A, k, 3, 4)
	'''
	for i in range(k+1):
		for j in range(k+1):
			findMaxInRange(A, k, i, j)
	'''
	
myAlgorithmTest()
