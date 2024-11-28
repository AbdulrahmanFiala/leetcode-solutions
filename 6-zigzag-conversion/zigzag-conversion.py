class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        if numRows == 1:
            return s
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                result += s[i]
                if (r > 0 and r < numRows - 1 and  i + increment - 2 * r < len(s)):
                    result += s[i + increment - 2 * r]
        return result

# Explanation Video (https://www.youtube.com/watch?v=Q2Tw6gcVEwc)
