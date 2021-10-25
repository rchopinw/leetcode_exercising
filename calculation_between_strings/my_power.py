# LC 50 power(x, n)
def power(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1/x
    if n%2:
        return power(x, n//2) * power(x, n//2 + 1)
    else:
        return power(x, n//2)**2

