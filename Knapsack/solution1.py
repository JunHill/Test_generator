# Values (stored in list v)
# Weights (stored in list w)
# Number of distinct items (n)
# Knapsack capacity W
def knapSack(v, w, n, W):

	# base case: Negative capacity
	if W < 0:
		return float('-inf')

	# base case: no items left or capacity becomes 0
	if n < 0 or W == 0:
		return 0

	# Case 1. include current item n in Knapsack (v[n]) and recur for
	# remaining items (n - 1) with decreased capacity (W - w[n])
	include = v[n] + knapSack(v, w, n - 1, W - w[n])

	# Case 2. exclude current item n from Knapsack and recur for
	# remaining items (n - 1)
	exclude = knapSack(v, w, n - 1, W)

	# return maximum value we get by including or excluding current item
	return max(include, exclude)


def solution(problem):
	return knapSack(problem["v"], problem["w"], len(problem["v"])-1, problem["W"])
