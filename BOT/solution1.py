def brute_force(seq,n):
    all_value = []
    prefix = [0]*n
    prefix[0]=seq[0]
    for i in range(1,n):
        prefix[i]=prefix[i-1]+seq[i]

    for p in range(0,n):
        for q in range(p,n):
            all_value.append({
                'p':p,
                'q':q,
                'value':prefix[q]-prefix[p-1] #the sum include p 
            })
    
    return max(all_value,key= lambda x:x['value'])
    

def solution(Problem):
    ans = brute_force(Problem["sequence"], len(Problem["sequence"]))
    return ans["p"]+1, ans["q"]+1, ans["value"]