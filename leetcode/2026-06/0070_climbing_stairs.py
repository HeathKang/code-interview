# Pattern: Constant-space DP
# Time: O(n)
# Space: O(1)
# Mistakes: The first version had the correct recurrence, but used recursion
# and a memo dictionary when only the previous two answers are needed.


class Solution:
    # Original Code:
    # class Solution:
    #     def climbStairs(self, n: int) -> int:
    #         memory = {}
    #         def dp(n: int) -> int:
    #             if memory.get(n) != None:
    #                 return memory.get(n)
    #             if n == 2:
    #                 memory[2] = 2
    #                 return 2
    #             elif n == 1:
    #                 memory[1] = 1
    #                 return 1
    #             elif n == 0:
    #                 memory[0] = 0
    #                 return 0
    #             else:
    #                 memory[n] = dp(n-1) + dp(n-2)
    #                 return memory[n]
    #
    #         return dp(n)
    #
    # Key Point:
    # Ways to reach step n equals ways to reach n - 1 plus ways to reach n - 2,
    # because the last move is either one step or two steps.
    #
    # Better Version:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one_step_before = 2
        two_steps_before = 1

        for _ in range(3, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current

        return one_step_before
