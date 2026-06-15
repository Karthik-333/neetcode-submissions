class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums==list(set(nums)) and k!=1:
            return nums
        res=[]
        freq=Counter(nums)
        arr=[]
        for key, values in freq.items():
            arr.append([values, key])
        arr.sort()
        while len(res) < k:
            res.append(arr.pop()[1])
        return res        