from typing import List


class Solution:
    # Original Code:
    # step = {}
    # for w in wordDict:
    #     if len(w) in step:
    #         step[len(w)].append(w)
    #     else:
    #         step[len(w)] = [w]
    #
    # Key Point:
    # Sort the dictionary buckets by word length so the recursion can stop
    # early when `n - num < 0`. This keeps the search focused on valid prefix
    # lengths first.
    #
    # Better Version:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        step = {}
        for w in wordDict:
            if len(w) in step:
                step[len(w)].append(w)
            else:
                step[len(w)] = [w]
        step = dict(sorted(step.items()))

        m = {}

        def dp(n):
            if n in m:
                return m.get(n)
            if n == 0:
                return True
            for num in step:
                if n - num < 0:
                    break
                if dp(n - num) and (s[n - num:n] in step[num]):
                    m[n] = True
                    return True
            m[n] = False
            return False

        return dp(len(s))
