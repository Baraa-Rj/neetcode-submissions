from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for string in strs:
            # Use sorted characters as the key (anagrams will have the same sorted form)
            key = tuple(sorted(string))
            anagram_map[key].append(string)

        return list(anagram_map.values())
