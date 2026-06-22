class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        l=[]
        for i,j in d.items():
            l.append([j,i])
        l.sort()
        res=[]
        while len(res)<k:
            res.append(l.pop()[1])
        return res

