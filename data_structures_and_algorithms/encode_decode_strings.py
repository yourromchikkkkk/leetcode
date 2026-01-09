from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStrs = ''
        for string in strs:
            encoded = f'{str(len(string))}#{string}'
            encodedStrs += encoded
        return encodedStrs


    def decode(self, s: str) -> List[str]:
        decoded, idx = [], 0

        while idx < len(s):
            j = idx
            while s[j] != '#':
                j += 1
            length = int(s[idx:j])
            decoded.append(s[j + 1:j + 1 + length])
            idx = j + 1 + length
        return decoded


solution = Solution()
testCase = ["Hello","World"]
encoded = solution.encode(testCase)
decoded = solution.decode(encoded)
print(decoded)