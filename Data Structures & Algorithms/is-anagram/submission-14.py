class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arrayOfS = [0]*26
        for ch in s:
            arrayOfS[ord(ch)-ord('a')] +=1
        arrayOfT = [0]*26
        for ch in t:
            arrayOfT[ord(ch)-ord('a')] +=1
        for i in range(26):
            if arrayOfS[i] != arrayOfT[i]:
                return False
        return True
        