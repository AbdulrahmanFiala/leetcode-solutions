class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        while right < len(nums):
            counter = 1
            while (right+1 < len(nums) and nums[right] == nums[right+1]):
                right +=1
                counter+=1
            for i in range(min(2, counter)):
                nums[left] = nums[right]
                left+=1
            right+=1
        return left

# Explantation Video (https://www.youtube.com/watch?v=ycAq8iqh0TI)