class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]

        for word in strs[1:]:
            i = 0
            while (i < len(word) 
            and i < len(longest_prefix)
            and word[i] == longest_prefix[i]
            ):
                i+=1
            longest_prefix = longest_prefix[:i]
        return longest_prefix
