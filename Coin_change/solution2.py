# Function to find the minimum number of coins required
# to get total of N from set S
def findMinCoins(S, N):

    # T[i] stores minimum number of coins needed to get total of i
    T = [0] * (N + 1)

    for i in range(1, N + 1):

        # initialize minimum number of coins needed to infinity
        T[i] = float('inf')

        # do for each coin
        for c in range(len(S)):
            # check if index doesn't become negative by including
            # current coin c
            if i - S[c] >= 0:
                res = T[i - S[c]]

                # if total can be reached by including current coin c,
                # update minimum number of coins needed T[i]
                if res != float('inf'):
                    T[i] = min(T[i], res + 1)

    # T[N] stores the minimum number of coins needed to get total of N
    return T[N]

def solution(Problem):
    coins =  findMinCoins(Problem["S"], Problem["N"])
    if coins != float('inf'):
        return coins
    else:
        return -1

