class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        for i in set(s) |set(t):
            if s.count(i) !=t.count(i):
                return False
        return True
        