
import random


def generate( length, capital=False, numbers=False, symbols=False, letters=True):
	if length < 1:
		return ""
	a = ""


	for i in range(length):
		a += chr(random.SystemRandom().randint(33, 126))

	a = list(a)
	for i in range(length):
		index1 = random.SystemRandom().randint(0, length-1)
		index2 = random.SystemRandom().randint(0, length-1)
		if index1 == index2:
			i -= 1
		a[index1], a[index2] = a[index2], a[index1]
	b = ""
	for i in a:
		b += i
	return b

	# Capital letters: 65-90
	# Small letters: 97-122
	# Numbers: 48-57
	# Symbols: 33-47, 58-64, 91-96, 123-126


def check_strength(string):

	categories = [0, 0, 0, 0]

	for i in range(len(string)):
		letter = ord(string[i])
		if 65 <= letter <= 90:  # Capital letters
			categories[0] = 1
		if 97 <= letter <= 122:  # Small letters
			categories[1] = 1
		if 48 <= letter <= 57:  # Numbers
			categories[2] = 1
		if 33 <= letter <= 47 or 58 <= letter <= 64 or 91 <= letter <= 96 or 123 <= letter <= 126:  # Symbols
			categories[3] = 1

	strength = len(string) * categories.count(1)

	if strength >= 32:
		return "Very strong"
	if strength >= 24:
		return "Strong"
	if strength > 15:
		return "Moderate"
	return "Weak"

a = "Very strong"
while a != "Weak":
	a = check_strength(generate(8))
	print(a)
