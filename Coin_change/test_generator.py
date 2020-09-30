import random
from math import floor
from solution2 import solution
# set a fixed random seed to re-create the same input file in the future 
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# set number of test cases
TEST_NUM = 40

# define constraints
CONSTRAINTS = {}
CONSTRAINTS["coin_value"] = 10**4
CONSTRAINTS["num_coin"] = 1000
CONSTRAINTS["total"] = 10**6


# generate groups of normal test cases
PERCENTAGE = {}
PERCENTAGE["test_set"] = [0.4, 0.7, 0.9, 1]
PERCENTAGE["num_coin"] = [0.25, 0.5, 0.75, 1]
PERCENTAGE["total"] = [0.0001, 0.001, 0.05, 1]
PERCENTAGE["coin_value"] = [0.0001, 0.001, 0.05, 1]

current_test = 0
last_coin_value = last_num_coin = last_total = 0

for p, p_num_coin, p_total, p_value in zip(PERCENTAGE["test_set"], PERCENTAGE["num_coin"], PERCENTAGE["total"], PERCENTAGE["coin_value"]):
	end = floor(p * TEST_NUM)
	for i in range(current_test, end):
		
		# Define a Problem
		Problem = {}
		Problem["N"] = random.randint(last_total, floor(p_total*CONSTRAINTS["total"]))
		Problem["S"] = []

		NUM_COIN = random.randint(last_num_coin, floor(p_num_coin*CONSTRAINTS["num_coin"]))
		for k in range(0, NUM_COIN):
			Problem["S"].append(random.randint(last_coin_value, floor(p_value*CONSTRAINTS["coin_value"])))

		# Write problem to file inp.txt
		inp = open("inp.txt", 'a')
		inp.write(str(Problem["N"]) + "\n")
		for item in Problem["S"]:
			inp.write("%s " % item)
		inp.write("\n")
		inp.close()

		# Write solution to file out.txt
		out = open("out.txt", 'a')
		out.write(str(solution(Problem)) + "\n")
		out.close()

		print(f"TEST {i} CREATED!")

	last_coin_value = floor(p_value*CONSTRAINTS["coin_value"])
	last_num_coin = floor(p_num_coin*CONSTRAINTS["num_coin"])
	last_total = floor(p_total*CONSTRAINTS["total"])
	current_test = end

