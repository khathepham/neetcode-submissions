class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = []

        for s in strs:
            found = False
            for sub in sublists:
                if self.anagramHash(s) == self.anagramHash(sub[0]):
                    sub.append(s)
                    found = True
            if not found:
                sublists.append([s])
        
        return sublists
    
    def anagramHash(self, s):
        h = {}
        for c in s:
            if c in h.keys():
                h[c] += 1
            else:
                h[c] = 1
        return h