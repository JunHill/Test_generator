
def salary(n, l)
    #n=int(input())
    #l=list(map(int,input().split()))
    m=max(l)
    c=0
    for j in range(n):
        if l[j]!=a:
            c=c+(a-l[j])
    return c


def solution(Problem):
	return salary(Problem["n"], Problem["l"])