#first try 
# def fix_try(s):
#     res = set()
#     l = 0
#     r = 0
#     for c in s:
#         if c == '(':
#             l += 1
#         elif c == ')':
#             if l > 0:
#                 l -= 1
#             else:
#                 r += 1

#     def dfs(s, i, left_count, right_count, left_rem, right_rem, curr):
#         if i == len(s):
#             if left_rem == 0 and right_rem == 0:
#                 res.add(curr)
#             return

#         c = s[i]

#         if c == '(':
#             if left_rem > 0:
#                 dfs(s, i + 1, left_count, right_count, left_rem - 1, right_rem, curr)
#             dfs(s, i + 1, left_count + 1, right_count, left_rem, right_rem, curr + c)
#         elif c == ')':
#             if right_rem > 0:
#                 dfs(s, i + 1, left_count, right_count, left_rem, right_rem - 1, curr)
#             if left_count > right_count:
#                 dfs(s, i + 1, left_count, right_count + 1, left_rem, right_rem, curr + c)
#         else:
#             dfs(s, i + 1, left_count, right_count, left_rem, right_rem, curr + c)

#     dfs(s, 0, 0, 0, l, r, "")
#     return list(res)

# print(fix_try("()())()"))  
# print(fix_try("(a)())()"))  
# print(fix_try("()"))        
# print(fix_try("abc"))    
# print(fix_try("(((")) 
# print(fix_try(")("))  

def fix_try(s):
    res = set()
    l = 0
    r = 0
    for c in s:
        if c == '(':
            l += 1
        elif c == ')':
            if l > 0:
                l -= 1
            else:
                r += 1

    def go(ss, i, lc, rc, lr, rr, cur):
        if i == len(ss):
            if lr == 0 and rr == 0:
                res.add(cur)
            return

        c = ss[i]

        if c == '(':

    def dfs(s, index, left_count, right_count, left_rem, right_rem, curr):
        if index == len(s):
            if left_rem == 0 and right_rem == 0:
                results.add(curr)
            return

        char = s[index]

        if char == '(':
            if left_rem > 0:
                dfs(s, index + 1, left_count, right_count, left_rem - 1, right_rem, curr)
            dfs(s, index + 1, left_count + 1, right_count, left_rem, right_rem, curr + char)
        elif char == ')':
            if right_rem > 0:
                dfs(s, index + 1, left_count, right_count, left_rem, right_rem - 1, curr)
            if left_count > right_count:
                dfs(s, index + 1, left_count, right_count + 1, left_rem, right_rem, curr + char)
        else:
            dfs(s, index + 1, left_count, right_count, left_rem, right_rem, curr + char)

    dfs(expr, 0, 0, 0, left, right, "")
    return list(results)
print(fix_exp("()())()"))  
print(fix_exp("(a)())()"))  
print(fix_exp(")("))  
print(fix_exp("()"))        
print(fix_exp("abc"))    
print(fix_exp("((("))      

def fix_exp(expr):
    results = set()
    left = 0
    right = 0
    for char in expr:
        if char == '(':
            left += 1
        elif char == ')':
            if left > 0:
                left -= 1
            else:
                right += 1

    def dfs(s, index, left_count, right_count, left_rem, right_rem, curr):
        if index == len(s):
            if left_rem == 0 and right_rem == 0:
                results.add(curr)
            return

        char = s[index]

        if char == '(':
            if left_rem > 0:
                dfs(s, index + 1, left_count, right_count, left_rem - 1, right_rem, curr)
            dfs(s, index + 1, left_count + 1, right_count, left_rem, right_rem, curr + char)
        elif char == ')':
            if right_rem > 0:
                dfs(s, index + 1, left_count, right_count, left_rem, right_rem - 1, curr)
            if left_count > right_count:
                dfs(s, index + 1, left_count, right_count + 1, left_rem, right_rem, curr + char)
        else:
            dfs(s, index + 1, left_count, right_count, left_rem, right_rem, curr + char)

    dfs(expr, 0, 0, 0, left, right, "")
    return list(results)
print(fix_exp("()())()"))  
print(fix_exp("(a)())()"))  
print(fix_exp(")("))  
print(fix_exp("()"))        
print(fix_exp("abc"))    
print(fix_exp("((("))      
