# LC 605: can place flowers
def can_place_flowers(flowerbed, n):
    if len(flowerbed) == 1:
        if n == 0 or (n == 1 and flowerbed[0] == 0):
            return True
        else:
            return False

    for i in range(len(flowerbed)):
        if i == 0 and flowerbed[i + 1] == flowerbed[i] == 0:
            flowerbed[i] = 1
            n -= 1
        elif i == len(flowerbed) - 1 and flowerbed[i - 1] == flowerbed[i] == 0:
            flowerbed[i] = 1
            n -= 1
        else:
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        if n <= 0:
            return True
    return False


def can_place_flowers_ii(flowerbed, n):
    s = len(flowerbed)
    bed = [0] + flowerbed + [0]

    for i in range(1, s + 1):
        if bed[i] == bed[i - 1] == bed[i + 1] == 0:
            bed[i] = 1
            n -= 1

        if n <= 0: return True

    return False
