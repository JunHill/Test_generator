import random
import string
from math import floor
from solution2 import solution
# set a fixed random seed to re-create the same input file in the future 
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# set number of test cases
TEST_NUM = 30

# define constraints
C_LENGTH = 10**4
C_LETTERS = string.ascii_uppercase
C_WORD_VARIATION = len(C_LETTERS)

# generate groups of normal test cases
PERCENTAGE_TEST_SET = [0.4, 0.7, 0.9, 1]
PERCENTAGE_LENGTH = [0.001, 0.01, 0.1, 1]
PERCENTAGE_VARIATION = [0.25, 0.5, 0.75, 1]

# Some helper variables
current_test = 0
last_length = last_variation = 0


for p, p_length, p_variation in zip(PERCENTAGE_TEST_SET, PERCENTAGE_LENGTH, PERCENTAGE_VARIATION):
	end = floor(p * TEST_NUM)
	for i in range(current_test, end):
		
		# Define a Problem
		Problem = {}
		Problem["X"] = "" 
		Problem["Y"] = ""

		LENGTH = random.randint(last_length, floor(p_length*C_LENGTH))
		for k in range(0, LENGTH):
			Problem["X"] += random.choice(C_LETTERS[0:floor(p_variation*C_WORD_VARIATION)])

		LENGTH = random.randint(last_length, floor(p_length*C_LENGTH))
		for k in range(0, LENGTH):
			Problem["Y"] += random.choice(C_LETTERS[0:floor(p_variation*C_WORD_VARIATION)])

		# Write problem to file inp.txt
		inp = open("inp.txt", 'a')
		inp.write(Problem["X"] + "\n")
		inp.write(Problem["Y"] + "\n")
		inp.close()

		# Write solution to file out.txt
		out = open("out.txt", 'a')
		out.write(str(solution(Problem)) + "\n")
		out.close()

		print(f"TEST {i} CREATED!")

	last_length = floor(p_length * C_LENGTH)
	last_variation = floor(p_variation * C_WORD_VARIATION)
	current_test = end

