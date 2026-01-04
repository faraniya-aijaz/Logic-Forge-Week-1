def product_except_self(contributions):
    n = len(contributions)
    impact = [1] * n

    # Left product
    for i in range(1, n):
        impact[i] = impact[i - 1] * contributions[i - 1]

    # Right product
    right = 1
    for i in range(n - 1, -1, -1):
        impact[i] = impact[i] * right
        right = right * contributions[i]

    return impact
print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1, 1, 0, -3, 3]))
