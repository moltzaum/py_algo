'''
Determine the probability that one dice will beat another.

A standard 6-sided dice would look like:
die = [1, 2, 3, 4, 5, 6]

However, the dices we will be comparing are:
D1 = [1, 8, 11, 14]
D2 = [2, 5, 12, 15]
D3 = [3, 6, 9, 16]
D4 = [4, 7, 10, 13]
'''

'''
Fraction:
init
toDecimal
getReciprocal
add
multiply
divide
simplify
str
'''
class Fraction:
	
	def __init__(self, numerator = 1, denominator = 1):
		self.numerator = numerator
		self.denominator = denominator
	
	def toDecimal(self):
		return self.numerator / self.denominator
	
	def getReciprocal(self):
		return Fraction(denominator, numerator);
		return self
		
	def add(self, frac):
		if (self.denominator == frac.denominator):
			self.numerator += frac.numerator
		else:
			self.numerator *= frac.denominator
			self.numerator += frac.numerator * self.denominator
			self.denominator *= frac.denominator
		return self
	
	def multiply(self, frac):
		self.numerator *= frac.numerator
		self.denominator *= frac.denominator
		return self
	
	#Test out this function
	def divide(self, frac):
		self.getReciprocal().multiply(frac)
		return self
	
	def simplify(self):
		gcd_ = gcd(self.numerator, self.denominator)		
		self.numerator = int(self.numerator / gcd_)
		self.denominator = int(self.denominator / gcd_)
		return self
	
	def __str__(self):
		return str(self.numerator) + '/' + str(self.denominator)

#Greatest Common Denominator
def gcd(x, y):
    if x % y == 0: return y
    else: return gcd(y, x % y)

def compareDice(die1, die2, chance_losing = True, print_chances = False):
	len_ = len(die1)
	frac_sum = Fraction(0, len_)
	for i in range(0, len_):
		num = 0
		for j in range(0, len_):
			if chance_losing:
				if die1[i] < die2[j]: num += 1
			else:
				if die1[i] > die2[j]: num += 1
		frac = Fraction(num, len_)
		
		if print_chances:
			print(str(die1[i]) + ' vs. ' + str(die2) + '\n\t ' + str(frac)
				+ (' chance of losing' if chance_losing else ' chance of winning'))
		frac_sum.add(frac)
	frac_sum.multiply(Fraction(1, len_))
	if print_chances: print('sum: ' + str(frac_sum))
	return frac_sum

def declareWinner(die1, die2, chance_losing = True, print_chances = False):
	
	frac = compareDice(die1[1], die2[1], chance_losing, print_chances)
	
	if frac.toDecimal() < 0.5 :
		print(die1[0] + ' wins over ' + die2[0])
	elif frac.toDecimal() > 0.5:
		print(die1[0] + ' loses to ' + die2[0])
	else:
		print (die1[0] + ' and ' + die2[0] + ' are tied!');

def main():
	
	D1 = [1, 8, 11, 14]
	D2 = [2, 5, 12, 15]
	D3 = [3, 6, 9, 16]
	D4 = [4, 7, 10, 13]
	#D4 > D3 > D2 > D1 > D4 ...
	
	name = ['dice 1', 'dice 2', 'dice 3', 'dice 4']
	dice = [D1, D2, D3, D4]
	
	for i in range(0, 4):
		print(name[i] + ': ' + str(dice[i]))
	print()
	
	for i in range(1, 4):
		print(name[0] + ' vs. ' + name[i] + ': ')
		print('Chance of dice 1 losing to ' + name[i] + ': ' + str(compareDice(dice[0], dice[i])))
		declareWinner([name[0], dice[0]], [name[i], dice[i]])
		print()
	
	'''
	print('***************************************')
	
	for i in range(0, 4):
		j = (i+1) % 4
		print(name[i] + ' vs. ' + name[j] + ': ')
		print('Chance of ' + name[i] + ' losing to ' + name[i] + ': ' + str(compareDice(dice[i], dice[j], True, True)))
		declareWinner([name[i], dice[i]], [name[j], dice[j]])
		print()
		
	print('***************************************')
	
	for i in range(0, 4):
		j = (i+1) % 4
		print(name[j] + ' vs. ' + name[i] + ': ')
		print('Chance of ' + name[j] + ' losing to ' + name[i] + ': ' + str(compareDice(dice[j], dice[i], True, True)))
		declareWinner([name[j], dice[j]], [name[i], dice[i]])
		print()
	'''
	
	for i in range(0, 4):
		print(name[i] + ' vs. ' + name[(i+1) % 4] + ': ')
		print('\t' + str(compareDice(dice[i], dice[(i+1) % 4])))
	
if __name__=="__main__":
   main()
   