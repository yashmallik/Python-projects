def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    buy_pointer = 0
    sell_pointer = 1
    while sell_pointer < (len(prices)):
        temp = prices[sell_pointer] - prices[buy_pointer]
        if prices[buy_pointer] < prices[sell_pointer]:
            profit = max(temp, profit)
        else:
            buy_pointer = sell_pointer
        sell_pointer += 1
    return profit
