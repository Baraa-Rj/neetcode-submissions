class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hashmap = defaultdict(list)
        for string in strs:
            my_hashmap[str(sorted(string))].append(string)
        return list(my_hashmap.values())
        
