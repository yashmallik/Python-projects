def jewelcount(jewels, stones):
    count = 0
    dictJewel = {}
    for i in jewels:
        dictJewel[i] = True

    for stone in stones:
        if stone in dictJewel:
            count += 1
    return count


jewels = "aA"
stones = "aAAbbb"
print(jewelcount(jewels, stones))
