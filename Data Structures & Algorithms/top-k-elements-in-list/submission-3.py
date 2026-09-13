class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums==list(set(nums)) and k!=0 :
            return nums
        res=[]
        freq=Counter(nums)
        for key, values in freq.items():
            if freq[key] >= k:
                res.append(key)
        return res        