# Pattern: Greedy / running tank balance
# Time: O(n)
# Space: O(1)
# Mistakes: The first version used an extra array and a final sum pass instead of
# tracking the total and current tank in one loop.

from typing import List


class Solution:
    # Original Code:
    # class Solution:
    #     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #         res = [0 for _ in gas]
    #         left = 0
    #         start = 0
    #         for i in range(len(gas)):
    #             res[i] = gas[i] - cost[i]
    #             left = res[i] + left
    #             if left < 0:
    #                 start = i + 1
    #                 left = 0
    #         if sum(res) < 0:
    #             return -1
    #         else:
    #             return start
    #
    # Key Point:
    # Keep the total gas-cost balance and the current tank balance in one pass.
    # If the tank goes negative, the current start cannot work.
    #
    # Better Version:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1
