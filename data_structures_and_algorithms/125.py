class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ', '')
        start, end = 0, len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue

            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

solution = Solution()
testCase = "A man, a plan, a canal: Panama"
testCase2 = "race a car"
testCase3 = "0P"
print(solution.isPalindrome(testCase3))