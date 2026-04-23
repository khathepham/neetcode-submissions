class Solution:

    def encode(self, strs: List[str]) -> str:
        en_str = ""
        for s in strs:
            en_str += str(len(s)) + "#" + s
        return en_str

    def decode(self, s: str) -> List[str]:
        strs = []
        while s != "":
            first_delim = s.find("#")
            len_sub = int(s[:first_delim])
            s = s[first_delim+1:]
            subs = s[:len_sub]
            s=s[len_sub:]
            strs.append(subs)
        return strs
