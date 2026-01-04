def min_window(log, pattern):
    if not log or not pattern:
        return ""
    
    need = {}
    for char in pattern:
        if char in need:
            need[char] += 1
        else:
            need[char] = 1
    
    window = {}
    left = 0
    have = 0
    required = len(need)
    
    min_len = float("inf")
    min_start = 0
    
    right = 0
    while right < len(log):
        char = log[right]
        if char in window:
            window[char] += 1
        else:
            window[char] = 1
        
        if char in need and window[char] == need[char]:
            have += 1
        
        while have == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            
            left_char = log[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                have -= 1
            
            left += 1
        
        right += 1
    
    if min_len == float("inf"):
        return ""
    return log[min_start:min_start + min_len]
print(min_window("ADOBECODEBANC", "ABC"))  
print(min_window("a", "aa"))               
print(min_window("a", "a"))               


