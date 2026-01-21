class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == 1:
            return 1
        
        seen = set()
        left, right = 0, 0
        maxL = 0

        while right < len(s):
            while s[right] not in seen:
                seen.add(s[right])
                maxL = max(maxL, right - left + 1)
                if right == len(s) - 1:
                    return maxL
                right += 1
            seen.remove(s[left])
            left += 1

        return maxL


solution = Solution()
testCase1 = "abcabcbb" # 3
testCase2 = "bbbbb" # 1
testCase3 = "au" # 2


print(solution.lengthOfLongestSubstring(testCase1))
print(solution.lengthOfLongestSubstring(testCase2))
print(solution.lengthOfLongestSubstring(testCase3))