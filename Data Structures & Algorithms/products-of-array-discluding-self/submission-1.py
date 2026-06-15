class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans=[0]*n
        # for i in range(len(nums)):
        #     res=1
        #     j=0
        #     while j<len(nums):
        #         if j!=i:
        #             res=res*nums[j]
        #         j+=1
        #     ans.append(res)
        # return ans   
        n=len(nums)
        ans=[]
        for i in range(len(nums)):
            j=0
            p=1
            while j<len(nums):
                if j!=i:
                    p*=nums[j]
                j+=1
            ans.append(p)    
        return ans        