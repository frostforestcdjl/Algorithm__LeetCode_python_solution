class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        have = False
        buy = 0
        profit = 0
        for i in range(len(prices)-1):
            if have == False:
                if prices[i] > prices[i+1]:
                    pass
                else:
                    buy = prices[i]
                    have = True
            else: 
                if prices[i] > prices[i+1]:
                    profit += prices[i] - buy
                    have = False
                else:
                    pass
        if have == True:
            profit += prices[-1] - buy
        return profit
