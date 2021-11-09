# LC 121: Max profit
def max_profit_i(prices):
    optimal = 0
    cur_min = float('inf')
    for price in prices:
        if cur_min > price:
            cur_min = price
        optimal = max(optimal, price - cur_min)
    return optimal


def max_profit_ii(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


def max_profit_iii(prices):
    t1_cost, t2_cost = float('inf'), float('inf')
    t1_profit, t2_profit = 0, 0
    for price in prices:
        t1_cost = min(t1_cost, price)
        t1_profit = max(t1_profit, price - t1_cost)
        t2_cost = min(t2_cost, price - t1_profit)
        t2_profit = max(t2_profit, price - t2_profit)
    return t2_profit


def max_profit_iv(prices):
    pass
