class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            if c not in d:
                return False
            if d[c] == 1:
                d.pop(c)
            else:
                d[c] -= 1
        return len(d) == 0