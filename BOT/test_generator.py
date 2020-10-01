import random
import string
from math import floor

from solution1 import solution
from 
# set a fixed random seed to re-create the same input file in the future 
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# set number of test cases
TEST_NUM = 50

# define constraints
CONSTRAINTS = {}
CONSTRAINTS["n"] = 10**6
CONSTRAINTS["a"] = 10**9

# generate groups of test cases
PERCENTAGE = {}
PERCENTAGE["test_set"] = [0.2, 0.4, 0.7, 0.9, 1]
PERCENTAGE["n"] = [0.00001, 0.0001, 0.001, 0.01, 1]
PERCENTAGE["a"] = [0.00001, 0.0001, 0.001, 0.01, 1]

# Some helper variables
current_test = 0
last_n = last_a = 0


for p, p_n, p_a in zip(PERCENTAGE["test_set"], PERCENTAGE["n"], PERCENTAGE["a"]):
	end = floor(p * TEST_NUM)

	# Start writing each test 
	for i in range(current_test, end):
		
		# Define a Problem
		Problem = {}
		Problem["sequence"] = []

		N = random.randint(last_n, floor(p_n*CONSTRAINTS["n"]))
		for k in range(0, N):
			Problem["sequence"].append(random.randint(-p_a * CONSTRAINTS["a"], p_a * CONSTRAINTS["a"]))

		# Write problem to file inp.txt
		inp = open("inp.txt", 'a')
		for item in Problem["sequence"]:
			inp.write("%s " % item)
		inp.write("\n")
		inp.close()

		# Write solution to file out.txt
		out = open("out.txt", 'a')
		out.write(str(solution(Problem)) + "\n")
		out.close()

		print(f"TEST {i} CREATED!")

	last_n = floor(p_n * CONSTRAINTS["n"])
	last_a = floor(p_a * CONSTRAINTS["a"])
	current_test = end
