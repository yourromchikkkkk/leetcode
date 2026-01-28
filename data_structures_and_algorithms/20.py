class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesMap = {')': '(', '}': '{', ']': '['}
        stack = list()

        for p in s:
            if p in parenthesesMap.values():
                stack.append(p)
            if p in parenthesesMap.keys():
                if not stack or parenthesesMap[p] != stack.pop():
                    return False
        
        return True if not stack else False
    
solution = Solution()
testCase = "()[]}{"
print(solution.isValid(testCase))
