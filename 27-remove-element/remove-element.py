class Solution:
    def removeElement(self, nums, val):
        counter = 0
        copy_list = nums.copy()
        for num in copy_list:
            if (num == val): 
                nums.remove(num)
            else: 
                counter += 1
        return counter
        
