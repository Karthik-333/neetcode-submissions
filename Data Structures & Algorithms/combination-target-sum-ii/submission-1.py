class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(start,comb,tot):
            if tot==target:
                res.append(comb[:])
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if tot+candidates[i]>target:
                    break
                comb.append(candidates[i])
                dfs(i+1,comb,tot+candidates[i])
                comb.pop()
        dfs(0,[],0)
        return res 