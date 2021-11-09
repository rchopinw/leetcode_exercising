def win(board, s):
    if any(x.count(s) == 3 for x in board):
        return True
    if any(''.join(x).count(s) == 3 for x in zip(*board)):
        return True
    if all(board[i][i] == s for i in range(3)) or all(board[i][2 - i] == s for i in range(3)):
        return True


def valid(board):
    total_x, total_o = 0, 0
    for row in board:
        total_x += row.count('X')
        total_o += row.count('O')
    if total_o > total_x or total_x - total_o >= 2:
        return False
    if total_x >= 3:
        if total_x == total_o and win(board, 'X'):
            return False
        if total_x > total_o and win(board, 'O'):
            return False
    return True
