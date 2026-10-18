class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(start,comb,total):
            if total==target:
                res.append(comb[:])
                return
            for i in range(start,len(nums)):
                if nums[i]+total>target:
                    break
                comb.append(nums[i])
                dfs(i,comb,nums[i]+total)
                comb.pop()
        dfs(0,[],0)
        return res                