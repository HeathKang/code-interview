# Pattern: Greedy / sum of positive differences
# Time: O(n)
# Space: O(1)
# Mistakes: The first attempt tracked a misleading "minPrice" variable and did not
# express the real invariant directly.

from typing import List


class Solution:
    # Original Code:
    # class Solution:
    #     def maxProfit(self, prices: List[int]) -> int:
    #         minPrice = prices[0]
    #         profit = 0
    #         for i in range(len(prices)):
    #             if prices[i] > minPrice:
    #                 profit = profit + prices[i] - minPrice
    #             minPrice = prices[i]
    #         return profit
    #
    # Key Point:
    # Every upward step can be captured independently. Sum each positive difference
    # between consecutive days.
    #
    # Better Version:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
