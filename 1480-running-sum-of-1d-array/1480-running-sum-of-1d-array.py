class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        j=1
        n=len(nums)
        while j< n:
            nums[j]=nums[j-1]+nums[j]
            
            j+=1
        return nums
        