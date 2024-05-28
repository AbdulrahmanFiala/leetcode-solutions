class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indices = []
        for i in range (len(nums)):
            for j in range (len(nums)):
                if (i==j):
                    continue
                if (nums[i] + nums[j] == target):
                    nums_indices.extend([i,j])
                    return nums_indices
                