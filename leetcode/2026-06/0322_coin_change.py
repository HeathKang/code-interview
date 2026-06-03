from typing import List


# Pattern: Top-down DP
# Time: O(amount * len(coins))
# Space: O(amount)
# Mistakes: The first version had the right idea, but repeated the same
# subproblem work inside one transition and used a more awkward sentinel flow.


class Solution:
    # Original Code:
    # class Solution:
    #     def coinChange(self, coins: List[int], amount: int) -> int:
    #         m = {}
    #         coins.sort(reverse=True)
    #
    #         def dp(n):
    #             if n in m:
    #                 return m[n]
    #
    #             if n == 0:
    #                 return 0
    #
    #             if n in coins:
    #                 m[n] = 1
    #                 return m[n]
    #
    #             temp = -1
    #             for c in coins:
    #                 if n - c < 0:
    #                     continue
    #                 if dp(n-c) != -1:
    #                     if temp != -1:
    #                         temp = min(dp(n-c)+1, temp)
    #                     else:
    #                         temp = dp(n-c)+1
    #             m[n] = temp
    #             return m[n]
    #
    #         return dp(amount)
    #
    # Key Point:
    # Define `dp(n)` as the minimum number of coins needed to form amount `n`.
    # Memoize each sub-amount, and sort coins so the recursion can stop early
    # once the current coin is larger than the remaining amount.
    #
    # Better Version:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        m = {}

        def dp(n):
            if n in m:
                return m[n]
            if n == 0:
                return 0

            temp = float("inf")
            for c in coins:
                if c > n:
                    break
                sub = dp(n - c)
                if sub != -1:
                    temp = min(temp, sub + 1)

            m[n] = -1 if temp == float("inf") else temp
            return m[n]

        return dp(amount)
