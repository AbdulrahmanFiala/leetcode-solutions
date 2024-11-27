class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for i in range(len(strs[0])):
            for str in strs:
                if i == len(str) or str[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

# Explanation Video (https://www.youtube.com/watch?v=0sWShKIJoo4)
        