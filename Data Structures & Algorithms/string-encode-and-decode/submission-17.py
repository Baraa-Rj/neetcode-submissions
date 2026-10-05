class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != "#":
                j += 1

            # Characters i:j contain the length
            length = int(s[i:j])

            # String starts after '#'
            start = j + 1
            end = start + length

            result.append(s[start:end])

            i = end

        return result