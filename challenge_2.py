#first try
# def min_window(log, pattern):
#     ans = ""
#     min_len = 10**9  

#     for i in range(len(log)):
#         for j in range(i, len(log)):
#             sub = log[i:j+1]

#             need = {}
#             for ch in pattern:
#                 if ch in need:
#                     need[ch] += 1
#                 else:
#                     need[ch] = 1

#             window = {}
#             for ch in sub:
#                 if ch in window:
#                     window[ch] += 1
#                 else:
#                     window[ch] = 1

#             ok = True
#             for ch in need:
#                 if ch not in window or window[ch] < need[ch]:
#                     ok = False

#             if ok:
#                 if len(sub) < min_len:
#                     min_len = len(sub)
#                     ans = sub

#     return ans
# print(min_window ("ADOBECODEBANC", "ABC"))

#second try
# def min_window(log, pattern):
#     ans = ""
#     min_len = 10**9

#     for i in range(len(log)):
#         for j in range(i, len(log)):
#             window = {}
#             for k in range(i, j+1):
#                 if log[k] in window:
#                     window[log[k]] += 1
#                 else:
#                     window[log[k]] = 1

#             need = {}
#             for ch in pattern:
#                 if ch in need:
#                     need[ch] += 1
#                 else:
#                     need[ch] = 1

#             match = True
#             for ch in need:
#                 if ch not in window or window[ch] < need[ch]:
#                     match = False

#             if match:
#                 if j - i + 1 < min_len:
#                     min_len = j - i + 1
#                     ans = log[i:j+1]

#     return ans
# print(min_window ("ADOBECODEBANC", "ABC"))



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



