class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s,count_t = Counter(s),Counter(t)

        return count_s == count_t




        

        