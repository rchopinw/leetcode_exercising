# LC 134: Gas station
def gas_station(gas, cost):
    if sum(cost) > sum(gas):
        return -1
    cur_gas, total_gas, start = 0, 0, 0
    for i, (g, c) in enumerate(zip(gas, cost)):
        cur_gas += g - c
        total_gas += g - c
        if cur_gas < 0:
            start = i + 1
            cur_gas = 0
    return start if total_gas >= 0 else -1

