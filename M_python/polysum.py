from math import tan
from math import pi
def polysum(n, s):
    A = (0.25 * n * s * s) / (tan(pi / n))
    P = s * n
    return round(A + (P * P), 4)

print(polysum(1, 2))