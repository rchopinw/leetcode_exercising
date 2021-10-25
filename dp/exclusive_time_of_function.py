# LC 636 Exclusive time of functions
def exclusive_time(n, logs):
    stack, dp = [], [0 for _ in range(n)]
    for log in logs:
        idx, status, timestamp = log.split(':')
        idx, timestamp = int(idx), int(timestamp)
        if not stack:
            stack.append([idx, status, timestamp])
        elif idx == stack[-1][0] and stack[-1][1] == 'start' and status == 'end':
            dp[idx] += timestamp - stack[-1][2] + 1
            stack.pop()
            if stack:
                stack[-1][2] = timestamp + 1
        else:
            dp[stack[-1][0]] += timestamp - stack[-1][2]
            stack.append([idx, status, timestamp])
    return dp


