#first try 
# def kth_smallest(matrix, k):
#     nums = []
#     for row in matrix:
#         for num in row:
#             nums.append(num)
#     nums.sort()    
#     return nums[k-1]
# matrix = [
#     [1, 5, 9],
#     [10, 11, 13],
#     [12, 13, 15]
# ]
# print(kth_smallest(matrix, 8)) 


def count_less_equal(matrix, mid):
    n = len(matrix)
    row, col = n - 1, 0
    count = 0
    while row >= 0 and col < n:
        if matrix[row][col] <= mid:
            count += row + 1 
            col += 1
        else:
            row -= 1
    return count

def kth_smallest_binary(matrix, k):
    n = len(matrix)
    low, high = matrix[0][0], matrix[-1][-1]
    
    while low < high:
        mid = (low + high) // 2
        if count_less_equal(matrix, mid) < k:
            low = mid + 1
        else:
            high = mid
    return low

#Test
matrix = [[1, 5, 9],
          [10, 11, 13],
          [12, 13, 15]]

print(kth_smallest_binary(matrix, 8))

