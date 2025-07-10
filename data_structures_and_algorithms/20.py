class Solution:
    def isValid(self, s: str) -> bool:
        parenthsesDict = {}
        for char in s:
            print(ord(char))
            if char in parenthsesDict:
                parenthsesDict[char] += 1
            else:
                parenthsesDict[char] = 1
        print(parenthsesDict)
        for count in parenthsesDict.values():
            if count % 2 != 1:
                return False
        return True
    
solution = Solution()
testCase = "()[]{}"
print(solution.isValid(testCase))
