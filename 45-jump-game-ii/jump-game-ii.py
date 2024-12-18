class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right= 0, 0
        minJumps = 0
        
        while right < len(nums) - 1:
            furthest = 0
            for i in range(left, right + 1):
                furthest = max(furthest, i + nums[i])
            left = right + 1
            right = furthest
            minJumps +=1
        return minJumps

# Exaplantatio Video: (https://www.youtube.com/watch?v=dJ7sWiOoK7g)