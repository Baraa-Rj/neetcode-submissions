from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for string in strs:
            count = [0] * 26  # 26 letters in the alphabet
            for char in string:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(string)  # Moved outside the inner loop

        return list(res.values())
