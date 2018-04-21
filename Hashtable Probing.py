'''
Consider inserting the keys
10, 22, 31, 4, 15, 28, 17, 88, 59
into a hash table of length m = 11 using open addressing with auxiliary hash function
h'(k) = k .

Illustrate the result of inserting these keys:
	while using linear probing,
	quadratic probing with c1 = 1 and c2 = 3, and
	double hashing with h1(k) = k and h2(k) = 1 + (k mod (m−1))

h' : U → {0, 1, . . . , m − 1} .
'''

m = 11

class LinearProbing:
	def __init__(self):
		global m
		self.slots = [None for _ in range(m)]

	def insert(self, key):
		global m
		i = 0
		while True:
			pos = (key + i) % m
			if self.slots[pos] is None:
				break
			i += 1
		self.slots[pos] = key


class QuadraticProbing:
	def __init__(self):
		global m
		self.slots = [None for _ in range(m)]

	def insert(self, key):
		global m
		i = 0
		while True:
			pos = (key + i + 3 * i * i) % m
			if self.slots[pos] is None:
				break
			i += 1
		self.slots[pos] = key


class DoubleHashing:
	def __init__(self):
		global m
		self.slots = [None for _ in range(m)]

	def insert(self, key):
		global m
		i = 0
		h2 = 1 + (key % (m - 1))
		while True:
			pos = (key + i * h2) % m
			if self.slots[pos] is None:
				break
			i += 1
		self.slots[pos] = key

input = [10, 22, 31, 4, 15, 28, 17, 88, 59]
lp = LinearProbing()
qp = QuadraticProbing()
dh = DoubleHashing()
for i in range(len(input)):
	lp.insert(input[i])
	qp.insert(input[i])
	dh.insert(input[i])
print('Keys to insert:\n', input)
print('Linear Probing:\n', lp.slots)
print('Quadratic Probing:\n', qp.slots)
print('Double Hashing:\n', dh.slots)
