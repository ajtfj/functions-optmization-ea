import math

def schwefel(x: list[float]):
    d = len(x)
    sum = 0
    for xi in x:
        sum += xi * math.sin(math.sqrt(abs(xi)))

    function = 418.9829 * d - sum
    return function