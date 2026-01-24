from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        windowFreqMap = defaultdict(int)
        left = 0
        
        maxF = 0
        for right in range(len(s)):
            windowFreqMap[s[right]] += 1
            maxF = max(maxF, windowFreqMap[s[right]])

            while (right - left + 1) - maxF > k:
                windowFreqMap[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)


        return res

            


solution = Solution()
testCase1 = "ABAB"
testCase2 = "AABABBA"
testCase3 = "ABBBAAB"
# print(solution.characterReplacement(testCase1, 2))
# print(solution.characterReplacement(testCase2, 1))
print(solution.characterReplacement(testCase3, 2))