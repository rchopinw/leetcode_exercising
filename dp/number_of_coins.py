# LC 518: Coin Change
def coin_change(amount, coins):
    dp = [1] + [0 for _ in range(amount)]
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[-1]


def coin_change_i(amount, coins):
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1
