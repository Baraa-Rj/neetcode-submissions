class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for string in strs:
            my_dict[tuple(sorted(string))].append(string)
        
        return list(my_dict.values())