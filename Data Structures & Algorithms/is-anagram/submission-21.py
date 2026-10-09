class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        t_sorted = "".join(sorted(t))
        s_sorted = "".join(sorted(s))
        for i in range(len(t_sorted)):
            if t_sorted[i] != s_sorted[i]:
                return False
        return True




        

        