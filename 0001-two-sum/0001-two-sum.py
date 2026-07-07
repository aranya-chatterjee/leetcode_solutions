class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # initiating a hash map 
        # hashMap={}
        # for index ,val in enumerate(nums): 
        #     #enumerate function index or uski valuue dono save karega
        #     diff=target-val
        #     if diff in hashMap: # agar diff hash map mei hua 
        #         return [hashMap[diff],index]  
        #         # returnn karega diff ka index and the num array ka index
        #     hashMap[val]=index #hash map ke anadr save karega element aur aage badhega
        # return None 





        hashMap={}
        for index , val in enumerate(nums):
            diff=target-val
            if diff in hashMap:
                return [hashMap[diff],index]
            hashMap[val]=index 
        return None 

       

      
       