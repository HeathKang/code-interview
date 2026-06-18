from collections import defaultdict
from typing import List


# Pattern: Hash map with canonical key
# Time: O(n * k log k), where k is the maximum string length
# Space: O(n * k)
# Mistakes: The first version used the right sorted-string key, but the file
# was missing the `List` import needed by its type annotations.


class Solution:
    # Original Code:
    # class Solution:
    #     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #         group = {}
    #         for s in strs:
    #             sorted_s = "".join(sorted(s))
    #             if sorted_s in group:
    #                 group[sorted_s].append(s)
    #             else:
    #                 group[sorted_s] = [s]
    #
    #         res = []
    #         for _, v in group.items():
    #             res.append(v)
    #         return res
    #
    # Key Point:
    # Anagrams have the same letters after sorting, so use the sorted string as
    # the hash-map key and collect every original word in that bucket.
    #
    # Better Version:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())
