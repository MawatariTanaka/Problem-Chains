def min_moves_bishop(M, N, x1, y1, x2, y2):
    if (x1, y1) == (x2, y2):
        return 0
    if (x1 + y1) % 2 != (x2 + y2) % 2:
        return -1
    if abs(x1 - x2) == abs(y1 - y2):
        return 1
    return 2