# https://leetcode.com/problems/coin-change/
# You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1

        MAX = float('inf')

        coins_needed = {i:MAX for i in range(1, amount+1)}
        coins_needed[0] = 0
    
        for change_amount in range(1, amount+1):
            available_coins = [c for c in coins if c <= change_amount]
            for coin in available_coins:
                coins_needed[change_amount] = min(coins_needed[change_amount], coins_needed[change_amount-coin]+1)
        if coins_needed[amount] == MAX:
            return -1
        else:
            return coins_needed[amount]
