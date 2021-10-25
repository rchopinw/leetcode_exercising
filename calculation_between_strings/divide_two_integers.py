# LC 29: divide two integers
def divide(dividend, divisor):
    MAX_INT = 2147483647
    MIN_INT = -2147483648
    HALF_MIN_INT = -1073741824

    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    powers_of_two = []
    doubles = []

    power_of_two = 0
    while dividend < divisor:
        powers_of_two.append(power_of_two)
        doubles.append(divisor)
        power_of_two += 1
        divisor += divisor

    answer = 0
    for i in reversed(range(len(doubles))):
        if doubles[i] >= dividend:
            dividend -= doubles[i]
            answer += powers_of_two[i]
    return answer if negatives != 1 else -answer
