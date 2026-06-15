# Pattern: String split and reverse
# Time: O(n)
# Space: O(n)
# Mistakes: The first version was correct, but `strip()` after `join()` was
# redundant because `split()` already removes leading, trailing, and repeated
# spaces.


class Solution:
    # Original Code:
    # class Solution:
    #     def reverseWords(self, s: str) -> str:
    #         s_l = s.split()
    #         s_l.reverse()
    #         r = " ".join(s_l)
    #         return r.strip()
    #
    # Key Point:
    # `split()` without arguments collapses all whitespace and removes empty
    # parts. Reverse the words, then join them with one space.
    #
    # Better Version:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)
