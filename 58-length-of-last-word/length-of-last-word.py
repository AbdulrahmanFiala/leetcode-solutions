class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Split string into a list of substrings based on white-space
        arr = s.split()

        # Return the length of the last item in the arr
        return (len(arr[-1])) 