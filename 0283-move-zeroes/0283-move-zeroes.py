class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        r=0
        n=len(nums)
        while r<n:
            if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                
                l+=1
            r+=1
        return nums 








        