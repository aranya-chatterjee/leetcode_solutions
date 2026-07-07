class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r=0,1
        # profit=0
        n=len(nums)
        max_profit=0
        while  r<n :
            if nums[l]>nums[r]:
                l=r
                # r+=1
            profit= nums[r]-nums[l]
            max_profit=max(max_profit, profit )
            r+=1
        return max_profit 
               