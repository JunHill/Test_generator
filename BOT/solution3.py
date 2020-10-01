
def BOT(t, n):
	t.insert(0,int(0))
	for i in range(1,n+1):
		t[i]=t[i]+t[i-1]

	maxx=-1000000
	p=0
	vtmax=0
	for i in t:
		p+=1
		if i>=maxx:
			maxx=i
			vtmax=p

	minn=1000000
	q=0
	vtmin=0
	for i in t[0:vtmax]:
		q+=1
		if i<minn:
			minn=i
			vtmin=q

	return (vtmin,vtmax-1,maxx-minn)

def solution(Problem):
	return BOT(Problem["sequence"], len(Problem["sequence"]))