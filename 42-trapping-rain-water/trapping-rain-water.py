class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        res = 0 
        
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(height[l], max_left)
                res+= max_left - height[l]
            else:
                r -= 1
                max_right = max(height[r], max_right)
                res+= max_right - height[r]
        return res

# Explanation Video (https://www.youtube.com/watch?v=ZI2z5pq0TqA)