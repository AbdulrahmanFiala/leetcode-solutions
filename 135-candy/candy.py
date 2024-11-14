class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyArr = [1] * len(ratings)
        for i in range (1, len(ratings)):
            if (ratings[i] > ratings[i-1]):
                candyArr[i] = candyArr[i-1] + 1

        for i in range (len(ratings)-2, -1, -1):
            if (ratings[i] > ratings[i+1]):
                candyArr[i] = max(candyArr[i], candyArr[i+1] + 1)
        return sum(candyArr)
        
# Explanation Video (https://www.youtube.com/watch?v=1IzCRCcK17A)
