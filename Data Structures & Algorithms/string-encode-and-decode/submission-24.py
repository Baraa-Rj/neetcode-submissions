class Solution:
   
    def encode(self,strs: List[str]) -> str:
        result = ""

        for string in strs:
            result += f"{len(string)}#{string}"

        return result


    def decode(self,s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            # Extract the length of the word
            length = int(s[i:j])

            # Extract the actual word
            start = j + 1
            word = s[start:start + length]
            result.append(word)

            # Skip the entire decoded word
            i = start + length

        return result