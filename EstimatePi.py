'''
This using the logic of making a graph and plotting random points
In a circle to find out the value
of Pi, the higher the digit you throw into the function,
the more accurate of an answer you will get.
'''

# Note: This is only done with numbers between 0 and 1 #
import random

# Note: The higher the number, the closer to pi it is. #
def EstimatePi(num):
    Dot_Total = 0
    Dots_In_Circle = 0
    for _ in range(num):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        Distance = x**2 + y**2
        if Distance <= 1:
            Dots_In_Circle += 1
        Dot_Total += 1
    return 4 * Dots_In_Circle / Dot_Total

print(EstimatePi(1_000_000))
