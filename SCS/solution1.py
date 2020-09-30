
# Function to find length of shortest Common supersequence of
# sequences X[0..m-1] and Y[0..n-1]
def SCSLength(X, Y, m, n):
 
    # if we have reached the end of either sequence, return
    # length of other sequence
    if m == 0 or n == 0:
        return n + m
 
    # if last character of X and Y matches
    if X[m - 1] == Y[n - 1]:
        return SCSLength(X, Y, m - 1, n - 1) + 1
 
    # last character of X and Y don't match
    return min(SCSLength(X, Y, m, n - 1) + 1, SCSLength(X, Y, m - 1, n) + 1)
 

def solution(Problem):
    return SCSLength(Problem["X"], Problem["Y"], len(Problem["X"]), len(Problem["Y"]))