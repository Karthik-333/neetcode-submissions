class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        # for s in strs:
        #     key=''.join(sorted(s))
        #     res[key].append(s)
        # return list(res.values())    
        for s in strs:
            count=[0]*26
            for ch in s:
                count[ord(ch)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())    

