import random
from math import floor
from solution2 import solution
# set a fixed random seed to re-create the same input file in the future 
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# set number of test cases
TEST_NUM = 40

# define constraints
C_TOTAL_WEIGHT = 10**6
C_WEIGHT = 10**5
C_VALUE = 10**3
C_NUM_OF_ITEM = 50
CONSTRANINTS = {}
CONSTRANINTS["total_weight"] = 10**6
CONSTRANINTS["weight"] = 10**5
CONSTRANINTS["value"] = 10**4
CONSTRANINTS["number_of_item"] = 50

# generate groups of test cases
PERCENTAGE = {}
PERCENTAGE["test_set"] = [0.2, 0.4, 0.6, 0.8, 1]
PERCENTAGE["number_of_item"] = [0.1, 0.25, 0.5, 0.75, 1]
PERCENTAGE["total_weight"] = [0.0001, 0.001, 0.01, 0.05, 1]
PERCENTAGE["weight"] = [0.0001, 0.001, 0.01, 0.05, 1]

current_test = 0
last_weight = last_value = last_num_of_item = last_total_weight = 0

for p, p_num, p_tot_weight, p_weight in zip(PERCENTAGE["test_set"], PERCENTAGE["number_of_item"], PERCENTAGE["total_weight"], PERCENTAGE["weight"]):
	end = floor(p * TEST_NUM)
	for i in range(current_test, end):
		
		# Define a Problem
		Problem = {}
		Problem["W"] = random.randint(last_total_weight, floor(p*C_TOTAL_WEIGHT))
		Problem['v'] = []
		Problem['w'] = []


		for k in range(0, floor(p_num*C_NUM_OF_ITEM)):
			Problem["v"].append(random.randint(0, C_VALUE))
		for k in range(0, floor(p_num*C_NUM_OF_ITEM)):
			Problem["w"].append(random.randint(last_weight, floor(p_weight*C_WEIGHT)))

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

