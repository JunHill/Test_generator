# Function to find length of shortest Common supersequence of
# sequences X[0..m-1] and Y[0..n-1]
def SCSLength(X, Y):

    m = len(X)
    n = len(Y)

    # lookup table stores solution to already computed sub-problems
    # i.e. T[i][j] stores the length of SCS of substring
    # X[0..i-1] and Y[0..j-1]
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]

    # initialize first column of the lookup table
    for i in range(m + 1):
        T[i][0] = i

    # initialize first row of the lookup table
    for j in range(n + 1):
        T[0][j] = j

    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1

            # else if current character of X and Y don't match
            else:
                T[i][j] = min(T[i - 1][j] + 1, T[i][j - 1] + 1)

    # SCS will be last entry in the lookup table
    return T[m][n]


def solution(Problem):
    return SCSLength(Problem["X"], Problem["Y"])
