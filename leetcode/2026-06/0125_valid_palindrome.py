# Pattern: Two pointers
# Time: O(n)
# Space: O(1)
# Mistakes: The first version was correct, but it built a filtered list instead
# of skipping non-alphanumeric characters in place.


class Solution:
    # Original Code:
    # class Solution:
    #     def isPalindrome(self, s: str) -> bool:
    #         s = [char for char in s if char.isalnum()]
    #
    #         if len(s) == 0:
    #             return True
    #         for i in range(len(s)//2+1):
    #             if s[i].lower() != s[len(s)-1-i].lower():
    #                 return False
    #
    #         return True
    #
    # Key Point:
    # Move two pointers inward. Skip characters that are not letters or digits,
    # and compare the remaining characters case-insensitively.
    #
    # Better Version:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
