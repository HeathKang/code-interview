# Pattern: Greedy symbol decomposition
# Time: O(1)
# Space: O(1)
# Mistakes: The first version was correct, but the positional indexing was harder
# to review than a direct value table.


class Solution:
    # Original Code:
    # class Solution:
    #     def intToRoman(self, num: int) -> str:
    #         symbol = {
    #             0: "",
    #             1: "MCXI",
    #             5: " DLV",
    #         }
    #         q = num // 1000
    #         b = num % 1000 // 100
    #         s = num % 100 // 10
    #         g = num % 10
    #
    #         numL = [q,b,s,g]
    #         res = ""
    #         for i in range(len(numL)):
    #             if numL[i] < 4:
    #                 res = res + symbol[1][i] * numL[i]
    #             elif numL[i] == 4:
    #                 res = res + symbol[1][i]+symbol[5][i]
    #             elif numL[i] == 5:
    #                 res = res + symbol[5][i]
    #             elif numL[i] > 5 and numL[i] < 9:
    #                 t = numL[i] % 5
    #                 res = res + symbol[5][i]+symbol[1][i]*t
    #             else:
    #                 res = res + symbol[1][i] + symbol[1][i-1]
    #
    #         return res
    #
    # Key Point:
    # Always take the largest Roman value that still fits. Include subtractive
    # forms like 900, 400, 90, 40, 9, and 4 directly in the table.
    #
    # Better Version:
    def intToRoman(self, num: int) -> str:
        symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = []
        for value, symbol in symbols:
            count, num = divmod(num, value)
            result.append(symbol * count)

        return "".join(result)
