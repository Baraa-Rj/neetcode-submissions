from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # <-- FIX: convert substring to integer
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res


