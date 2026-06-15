class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            res=1
            j=0
            while j<len(nums):
                if j!=i:
                    res=res*nums[j]
                j+=1
            ans.append(res)
        return ans   