# Pattern: Stack
# Time: O(n)
# Space: O(n)


class Solution:
    # Original Code:
    # class Solution:
    #     def isValid(self, s: str) -> bool:
    #         pair = {"]": "[", ")": "(", "}": "{"}
    #         b = []
    #         for char in s:
    #             match char:
    #                 case "(" | "[" | "{":
    #                     b.append(char)
    #                 case ")" | "]" | "}":
    #                     if len(b) < 1:
    #                         return False
    #                     t = b.pop(-1)
    #                     if t != pair[char]:
    #                         return False
    #         if len(b) == 0:
    #             return True
    #         return False
    #
    # Key Point:
    # Push opening brackets onto a stack. Each closing bracket must match the
    # most recent opening bracket, and the stack must be empty at the end.
    #
    # Better Version:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return not stack
