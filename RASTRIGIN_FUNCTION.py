import math

def rastrigin(x: list[float]):
    d = len(x)
    sum = 0
    for xi in x:
        sum += (xi*xi) - 10 * math.cos(2*math.pi*xi)
    
    function = 10*d + sum
    return function