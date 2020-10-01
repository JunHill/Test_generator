def salary(n, l)
    #n=int(input())
    #l=list(map(int,input().split()))
    l.sort()
    c=0
    min=l[0]
    for j in range(1,len(l)):
        c=c+(l[j]-min)
    return c


def solution(Problem):
	return salary(Problem["n"], Problem["l"])