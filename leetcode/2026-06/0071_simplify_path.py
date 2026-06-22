# Pattern: Stack
# Time: O(n)
# Space: O(n)
# Mistakes: The original file contained the solution for Valid Parentheses and
# did not provide the required `simplifyPath` method.


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
    # Split the path by `/`. Ignore empty parts and `.`, pop one directory for
    # `..` when possible, and push every normal directory name.
    #
    # Better Version:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != ".":
                stack.append(part)

        return "/" + "/".join(stack)
