class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # var holds count of letters of last word in string
        counter = 0
        # var verfies if we skipped the last white-spaces
        flag = True
        # var to reverse-traverse through string
        reversed_index = -1

        for i in range(len(s)):
            
            # verify if reached the last word or not
            if (flag and s[reversed_index] == " "):
                reversed_index -=1
                continue
            
            # reached the last word in string 
            flag = False            
                
            # increment the counter since we caught the last word
            if (not s[reversed_index] == " "):
                counter +=1
            
            
            # verify if we reached the end of the last word
            if (s[reversed_index] == " " or i + 1 == len(s)):
                return counter
                
            # decrement the index to move to the next letter
            reversed_index -=1
