class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        path=[]
        def backtracking(i):
            res.append(path[:])
                # return        // return function nahi aayega 
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                path.append(nums[j])
                backtracking(j+1)
                path.pop()
        
        backtracking(0)
        return res