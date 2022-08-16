from numpy import random

print("Result:\n", a := random.binomial(1, 0.1, 1))

print("Count: ", N := sum(a))