class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(l,r):
            if l==r:
                res.append(nums[:])
                return
            for i in range(l,r):
                nums[l],nums[i]=nums[i],nums[l]
                backtrack(l+1,r)
                nums[l],nums[i]=nums[i],nums[l]
        backtrack(0,len(nums))
        return res        