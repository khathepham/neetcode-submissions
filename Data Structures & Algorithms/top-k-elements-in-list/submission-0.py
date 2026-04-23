class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        l = []
        for i in range(0, k):
            key = max(d, key=d.get)
            l.append(key)
            d.pop(key)
        return l
        