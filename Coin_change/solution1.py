# Function to find the minimum number of coins required
# to get total of N from set S
def findMinCoins(S, N):

    # if total is 0, no coins are needed
    if N == 0:
        return 0

    # return INFINITY if total become negative
    if N < 0:
        return float('inf')

    # initialize minimum number of coins needed to infinity
    coins = float('inf')

    # do for each coin
    for i in range(len(S)):

        # recur to see if total can be reached by including
        # current coin S[i]
        res = findMinCoins(S, N - S[i])

        # update minimum number of coins needed if choosing current
        # coin resulted in solution
        if res != float('inf'):
            coins = min(coins, res + 1)

    # return minimum number of coins needed
    return coins
    
def solution(Problem):
    coins =  findMinCoins(Problem["S"], Problem["N"])
    if coins != float('inf'):
        return coins
    else:
        return -1


