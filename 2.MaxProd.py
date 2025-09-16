# Given an array of N integer
# Find the highest product by multiplying 3 elements
# Constraint 3 <= N <= 5e^5

def maxProdBy3(l):
    sorted(l)
    x1 = l[-1] * l[-2] * l[-3]
    x2 = l[0] * l [1] * l [len(l)-1]
    return max(x1, x2)

print(maxProdBy3([1,2,3,4]))
print(maxProdBy3([0, -1, 10, 5, 7]))
print(maxProdBy3([-5, -2, -1, 0, 0, 3, 4, 5]))
print(maxProdBy3([-5, -2, -1, 0, 0, 1, 1, 5]))