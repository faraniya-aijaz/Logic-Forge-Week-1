# FIRST TRY
# def contributions(arr):
#     result = []
#     for i in range(len(arr)):
#         prod = 1
#         for j in range(len(arr)):
#             if i != j:
#                 prod *= arr[j]
#         result.append(prod)
#     return result
# arr1 = [1, 2, 3, 4]
# arr2 = [-1, 1, 0, -3, 3]

# print(contributions(arr1)) 
# print(contributions(arr2)) 

# SECOND
def Team_Contributions(contributions):
    n = len(contributions)
    impact = [1] * n
    for i in range(1, n):
        impact[i] = impact[i - 1] * contributions[i - 1]
    right = 1
    for i in range(n - 1, -1, -1):
        impact[i] = impact[i] * right
        right = right * contributions[i]

    return impact
print(Team_Contributions([1, 2, 3, 4]))
print(Team_Contributions([-1, 1, 0, -3, 3]))
