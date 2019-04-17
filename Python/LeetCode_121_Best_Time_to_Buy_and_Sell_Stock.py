# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('Inf')
        profit = 0
        
        for price in prices:
            buy_price = min(buy_price, price)
            profit = max(profit, price-buy_price)
            
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_min = float('Inf')
        price_max = float('-Inf')
        profit_max = 0
        
        for price in prices:
            if price < price_min:
                price_min = price
                price_max = price
                continue
                
            if price > price_max:
                price_max = price
                profit_temp = price_max - price_min
            else:
                continue
                
            if profit_temp > profit_max:
                profit_max = profit_temp
                
        return profit_max