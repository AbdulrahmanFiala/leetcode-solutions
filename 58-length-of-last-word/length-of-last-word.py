class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # remove leading and trailing spaces
        s = s.strip()

        # Find the index of the last space
        last_space_index = s.rfind(" ")

        # Return the length of the last word
        return (len(s) - 1) - last_space_index