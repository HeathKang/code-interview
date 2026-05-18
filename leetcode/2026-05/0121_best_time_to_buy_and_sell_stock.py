# Pattern: Greedy / one-pass minimum tracking
# Time: O(n)
# Space: O(1)
# Mistakes: Brute-force checked every buy/sell pair; keep only the lowest price seen so far.

from typing import List


class Solution:
    # Original Code:
    # class Solution:
    #     def maxProfit(self, prices: List[int]) -> int:
    #         profit = 0
    #         for i in range(len(prices)-1):
    #             for j in range(i+1, len(prices)):
    #                 if prices[j] - prices[i] > profit:
    #                     profit = prices[j] - prices[i]
    #         return profit
    #
    # Key Point:
    # Track the best buy price so far. For each day, the best profit ending today
    # is current price minus the minimum prior price.
    #
    # Better Version:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                best = max(best, price - min_price)

        return best
