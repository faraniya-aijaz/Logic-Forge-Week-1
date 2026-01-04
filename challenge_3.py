def find_median(scoresA, scoresB):
    m = len(scoresA)
    n = len(scoresB)
    total = m + n
    mid_index = total // 2
    
    i = 0
    j = 0
    prev = 0
    curr = 0
    
    for count in range(mid_index + 1):
        prev = curr
        if i < m and (j >= n or scoresA[i] <= scoresB[j]):
            curr = scoresA[i]
            i += 1
        else:
            curr = scoresB[j]
            j += 1
            
    if total % 2 == 1:
        return float(curr)
    else:
        return (prev + curr) / 2
print(find_median([1, 3], [2]))        
print(find_median([1, 2], [3, 4]))   
