# LC 121: Max profit
def max_profit(prices):
    optimal = 0
    cur_min = float('inf')
    for price in prices:
        if cur_min > price:
            cur_min = price
        optimal = max(optimal, price - cur_min)
    return optimal
