import random
import string
from math import floor

from solution2 import solution

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

file = open("out.txt", 'r')
for p, p_n, p_a in zip(PERCENTAGE["test_set"], PERCENTAGE["n"], PERCENTAGE["a"]):
	end = floor(p * TEST_NUM)
	for i in range(current_test, end):
		
		# Define a Problem
		Problem = {}
		Problem["sequence"] = []

		N = random.randint(last_n, floor(p_n*CONSTRAINTS["n"]))
		for k in range(0, N):
			Problem["sequence"].append(random.randint(-p_a * CONSTRAINTS["a"], p_a * CONSTRAINTS["a"]))

		res = str(solution(Problem))
		line = file.readline()
		if not line:
			break;
		try:
			assert res+"\n" == line
			print(f"Passed test {i}")
		except:
			print(f"Failed Test {i}, Expect {line} , Got {res}")

	last_n = floor(p_n * CONSTRAINTS["n"])
	last_a = floor(p_a * CONSTRAINTS["a"])
	current_test = end
