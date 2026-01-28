from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        
        resLen, resRange = float("infinity"), [-1, -1]
        needMap, windowMap = defaultdict(int), defaultdict(int)
        windowCount, left = 0, 0
        
        for char in t:
            needMap[char] += 1
        
        needCount = len(needMap)

        for right in range(len(s)):
            rightChar = s[right]
            windowMap[rightChar] += 1
            if rightChar in t and windowMap[rightChar] == needMap[rightChar]:
                windowCount += 1

            while needCount == windowCount:
                leftChar = s[left]
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    resRange = [left, right]
                if leftChar in windowMap:
                    windowMap[leftChar] -= 1
                if s[left] in t and windowMap[leftChar] < needMap[leftChar]:
                    windowCount -= 1
                left += 1

        
        return s[resRange[0]:resRange[1] + 1] if resLen != float("infinity") else ""
        


solution = Solution()
testS1 = 'ADOBECODEBANC'
testT1 = 'ABC'
testS2 = 'a'
testT2 = 'a'
print(solution.minWindow(testS2, testT2))