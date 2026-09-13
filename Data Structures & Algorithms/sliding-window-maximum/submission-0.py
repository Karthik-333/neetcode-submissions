class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Max=0
        res=[]
        index=len(nums)-k
        for i in range(index+1):
            Max=max(nums[i:k])
            res.append(Max)
            k+=1
        return res    