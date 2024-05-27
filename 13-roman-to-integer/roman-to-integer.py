class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            char = s[i]
            next_char = "placeholder"
            if(i < len(s) - 1):
                next_char = s[i+1]

            if (char == "I"):
                sum+= 1
                if(next_char == "V" or next_char == "X"):
                    sum-= 2

            elif (char == "V"):
                sum+= 5

            elif (char == "X"):
                sum+=10
                if(next_char == "L" or next_char == "C"):
                    sum-= 20

            elif (char == "L"):
                sum+=50

            elif (char == "C"):
                sum+=100
                if(next_char == "D" or next_char == "M"):
                    sum-= 200

            elif (char == "D"):
                sum+=500

            elif (char == "M"):
                sum+=1000

        return sum