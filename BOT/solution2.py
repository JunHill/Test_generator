def kadane(seqs):

  max_sum_present = 0

  max_sum_ending_at = 0

  start_index = 0

  start_temp = -1
  ending_index = 0

  for i in range(len(seqs)):
  
    max_sum_ending_at += seqs[i]
    if (max_sum_ending_at < 0):
      max_sum_ending_at = 0
      start_temp = -1
    else:
      if start_temp == -1:
        start_temp = i
      if max_sum_present < max_sum_ending_at:
        max_sum_present = max_sum_ending_at
        start_index = start_temp
        ending_index = i
  return start_index+1, ending_index+1, max_sum_present 


def solution(Problem):
	start, stop, profit = kadane(Problem["sequence"]) 
	return  start, stop, profit