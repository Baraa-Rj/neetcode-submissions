class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        sizes = []

        for string in strs:
            sizes.append(str(len(string)))

        return ''.join(['\\'.join(i) for i in zip(sizes, strs)])

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0

        while i < len(s):
            delimiter_index = s[i:].index("\\")
            length = int(s[i : i + delimiter_index])
            decoded.append(
                s[i + delimiter_index + 1 : i + delimiter_index + length + 1]
            )
            i = i + delimiter_index + length + 1

        return decoded