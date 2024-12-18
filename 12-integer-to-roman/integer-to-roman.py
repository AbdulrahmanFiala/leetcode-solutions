class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [["I", 1],  ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100]
        ,["CD", 400], ["D", 500], ["CM", 900], ["M",1000]]
        
        res = ""
        for symbol, val in reversed(roman):
            if (num//val):
                count = num//val
                res+= count * symbol
                num = num%val
        return res

# Explanation Video (https://www.youtube.com/watch?v=ohBNdSJyLh8)