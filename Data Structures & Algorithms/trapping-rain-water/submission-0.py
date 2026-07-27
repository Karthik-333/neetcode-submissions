class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        max_left=height[l]
        max_right=height[r]
        while l<r:
            if max_left<max_right:
                l+=1
                max_left=max(height[l],max_left)
                res+=max_left-height[l]
            else:
                r-=1
                max_right=max(height[r],max_right)
                res+=max_right-height[r]
        return res