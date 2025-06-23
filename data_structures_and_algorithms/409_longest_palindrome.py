class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        counterMap = {}
        for letter in s:
            counterMap[letter] = 1 if letter not in counterMap.keys() else counterMap[letter] + 1
        
        maxLengths = 0
        for value in counterMap.values():
            if value == 1 and maxLengths % 2 == 0:
                maxLengths += 1
            if value % 2 == 0:
                maxLengths += value
            if value % 2 == 1 and value != 1:
                maxLengths += value
        return maxLengths


solution = Solution()
testCase = 'ccd'
print(solution.longestPalindrome(testCase))