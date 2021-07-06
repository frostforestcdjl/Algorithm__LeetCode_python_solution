class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def check_profits(prices):
            try:
                if prices.index(max(prices)) > prices.index(min(prices)):
                    return max(prices) - min(prices)
                else:
                    return 0
            except:
                return 0
        
        if check_profits(prices) != 0:
            return check_profits(prices)
        

        
        def clean_sides(row_prices):
            try:
                while (row_prices[0] > row_prices[1]):
                    row_prices.pop(0)
            except:
                pass
            try:
                while (row_prices[-1] < row_prices[-2]):
                    row_prices.pop()
            except:
                pass
            return row_prices
        
        prices = clean_sides(prices)
        
        if prices.index(max(prices)) == prices.index(min(prices)):
            return 0
        
        if len(prices) <= 1:
            return 0
        
        zone_1 = prices[0:prices.index(max(prices))+1]
        try:
            zone_2 = prices[prices.index(max(prices))+1:prices.index(min(prices))]
        except:
            zone_2 = [0]
        zone_3 = prices[prices.index(min(prices)):]

        prifit = []
        profit_1 = check_profits(clean_sides(zone_1))
        profit_2 = check_profits(clean_sides(zone_2))
        profit_3 = check_profits(clean_sides(zone_3))
        
        if (profit_1 + profit_2 + profit_3) != 0:
            return max(profit_1, profit_2, profit_3)
        
        profit = [profit_1, profit_2, profit_3]
        try:
            for j in range(3):
                for i in range(1, len(profit[j]) - 1):
                    while ((profit[j][i] != max(profit[j][i-1], profit[j][i], profit[j][i+1])) and (profit[j][i] != min(profit[j][i-1], profit[j][i], profit[j][i+1]))):
                        profit[j].pop(i)
        except:
            pass
    
        temp_max = 0
        for j in range(3):
            for i in range(len(profit[j])):
                diff = max(profit[j]) - profit[j][0]
                if diff > temp_max:
                    temp_max = diff
                profit[j].pop(0)
        return temp_max
