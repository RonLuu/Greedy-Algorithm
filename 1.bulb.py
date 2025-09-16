# Given N bulbs, either on (1) or off (0).
# Turning on the ith bulb causes all remaining bulbs on the right to flip

# Find the min number of switches to turn all the bulbs on
# Contraints
# 1 <= N <= 1e5
# A[i] = {0,1}

def bulbs(A):
    cost = 0
    for bulb in A:
        if cost % 2 == 0:
            bulb = bulb
        else:
            bulb = not bulb
        
        if bulb == 1:
            continue
        else: 
            cost += 1
    return cost