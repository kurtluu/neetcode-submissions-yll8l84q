class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += '|' + s
        return res
        

    def decode(self, s: str) -> List[str]:
        strs = []
        strs = s.split('|')
        strs.pop(0)
        return strs