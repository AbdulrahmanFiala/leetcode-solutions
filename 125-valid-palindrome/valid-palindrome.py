import re

class Solution:
    def filtering_string(self, s: str) -> str:
        pattern = '[a-zA-Z0-9]'
        reg_exp = re.compile(pattern)
        filtered_string =""

        for char in reg_exp.findall(s):
            filtered_string = filtered_string + char.lower() 

        return filtered_string

    def isPalindrome(self, s: str) -> bool:
        filtered_string = self.filtering_string(s)
        start = 0
        end = len(filtered_string) -1

        while start <= end:
            if (not (filtered_string[start] == filtered_string[end]) ):
                return False
            start +=1
            end -=1

        return True 
            
