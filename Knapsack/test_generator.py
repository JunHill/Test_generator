import random
from math import floor
from solution2 import solution
# set a fixed random seed to re-create the same input file in the future 
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# set number of test cases
TEST_NUM = 40

# define constraints
C_TOTAL_WEIGHT = 5* (10**5)
C_WEIGHT = 10**5
C_VALUE = 10**3
C_NUM_OF_ITEM = 50


# generate groups of normal test cases
PERCENTAGE_TEST_SET = [0.2, 0.5, 0.8, 1]

current_test = 0
last_weight = last_value = last_num_of_item = last_total_weight = 0

for p in PERCENTAGE_TEST_SET:
	end = floor(p * TEST_NUM)
	for i in range(current_test, end):
		
		# Define a Problem
		Problem = {}
		Problem["W"] = random.randint(last_total_weight, floor(p*C_TOTAL_WEIGHT))
		Problem['v'] = []
		Problem['w'] = []


		for k in range(0, floor(p*C_NUM_OF_ITEM)):
			Problem["v"].append(random.randint(last_value, floor(p*C_VALUE)))
		for k in range(0, floor(p*C_NUM_OF_ITEM)):
			Problem["w"].append(random.randint(last_weight, floor(p*C_WEIGHT)))

		# Write problem to file inp.txt
		inp = open("inp.txt", 'a')
		inp.write(str(Problem["W"]) + "\n")
		for item in Problem["v"]:
			inp.write("%s " % item)
		inp.write("\n")
		for item in Problem["w"]:
			inp.write("%s " % item)
		inp.write("\n")
		inp.close()

		# Write solution to file out.txt
		out = open("out.txt", 'a')
		out.write(str(solution(Problem)) + "\n")
		out.close()

		print(f"TEST {i} CREATED!")

	last_value = floor(p*C_VALUE)
	last_weight = floor(p*C_WEIGHT)
	last_num_of_item = floor(p*C_NUM_OF_ITEM)
	last_total_weight = floor(p*C_TOTAL_WEIGHT)
	current_test = end

