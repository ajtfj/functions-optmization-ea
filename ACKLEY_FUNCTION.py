import math

def ackley(x:list[float]):
    a, b, c = 20, 0.2, 2 * math.pi
    d = len(x)
    sum1 = 0
    sum2 = 0
    for xi in x:
        sum1 += xi*xi
        sum2 += math.cos(c*xi)

    first_term = -a * math.exp(-b*math.sqrt(sum1/d))
    second_term = -1 * math.exp(sum2/d)
    function = first_term + second_term + a + math.exp(1)
    return function