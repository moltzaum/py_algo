
# This is a program that tries to decode a section of morse code by creating a list
# of all possible permutations. It is not a standard decoding of morse that determines
# the end of a word with spaces. I could make the algorithm more efficient if I used
# markov chains.

A = '.-'
B = '-...'
C = '-.-.'
D = '-..'
E = '.'
F = '..-.'
G = '--.'
H = '....'
I = '..'
J = '.---'
K = '-.-'
L = '.-..'
M = '--'
N = '-.'
O = '---'
P = '.--.'
Q = '--.-'
R = '.-.'
S = '...'
T = '-'
U = '..-'
V = '...-'
W = '.--'
X = '-..-'
Y = '-.--'
Z = '--..'

d1 = '.----'
d2 = '..---'
d3 = '...--'
d4 = '....-'
d5 = '.....'
d6 = '-....'
d7 = '--...'
d8 = '---..'
d9 = '----.'
d0 = '-----'

alphabet = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
digits = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d0]

def getAlpha(morse_letter):
	return {
		A: 'A',
		B: 'B',
		C: 'C',
		D: 'D',
		E: 'E',
		F: 'F',
		G: 'G',
		H: 'H',
		I: 'I',
		J: 'J',
		K: 'K',
		L: 'L',
		M: 'M',
		N: 'N',
		O: 'O',
		P: 'P',
		Q: 'Q',
		R: 'R',
		S: 'S',
		T: 'T',
		U: 'U',
		V: 'V',
		W: 'W',
		X: 'X',
		Y: 'Y',
		Z: 'Z'
	}[morse_letter]

def getMorse(char):
	return {
		'A': A,
		'B': B,
		'C': C,
		'D': D,
		'E': E,
		'F': F,
		'G': G,
		'H': H,
		'I': I,
		'J': J,
		'K': K,
		'L': L,
		'M': M,
		'N': N,
		'O': O,
		'P': P,
		'Q': Q,
		'R': R,
		'S': S,
		'T': T,
		'U': U,
		'V': V,
		'W': W,
		'X': X,
		'Y': Y,
		'Z': Z,
		'1': d1,
		'2': d2,
		'3': d3,
		'4': d4,
		'5': d5,
		'6': d6,
		'7': d7,
		'8': d8,
		'9': d9,
		'0': d0,
		' ': ''
	}[char]

file = open("output.txt", "w")

'''
ALGORITHM
-.--.-...
found B at back
>> (put into process queue)
    B (-...)
    -.--.

-.--.-...
found E back
>> (put into process queue)
	E (.)
	-.--.-..
	-.--
continue...
the alphabet is exhausted
'''
def decode(input, char_rep = ""):
	global alphabet
	global file
	
	if len(input) == 0: #We exhausted the concrete options
		file.write(char_rep + '\n')
	
	for letter in alphabet:
		if input.endswith(letter):
			# continue with removed letter, and add letter to char array
			decode(input[:-len(letter)], getAlpha(letter) + char_rep)

def encode(input):
	result = ""
	for letter in input:
		result += getMorse(letter) + ' '
	return result
	
# Hmmm.. Maybe its EEETETTETT?
decode("...-.--.--") # STAY or SKY
#print(encode("STAY"))
#print(encode("SKY"))

