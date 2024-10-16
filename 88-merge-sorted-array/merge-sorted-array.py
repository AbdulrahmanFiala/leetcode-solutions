class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums2)):
            for j in range(m+n):
                if(nums2[i] < nums1[j] or j == m +i):
                    nums1.insert(j, nums2[i])
                    break
        nums1[:] = nums1[0:n+m]