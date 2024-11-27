class Solution:
    def reverseWords(self, s: str) -> str:
        result, i, n = "", 0, len(s)
        while i < n:
            while i < n and s[i] == " ":
                i+=1
            j = i + 1
            while j < n and s[j] != " ":
                j += 1
            word = s[i:j]
            if result == "":
                result = word
            elif i < n:
                result = word + " " + result
            i = j
        return result

# Explanation Video (https://www.youtube.com/watch?v=vhnRAaJybpA)
