from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        sliceStart = 0
        result = []
        while sliceStart < len(s):
            for idx in range(len(s)):
                if idx + 1 != len(s) and (idx + 1) % k == 0:
                    result.append(s[sliceStart:idx+1])
                    sliceStart = idx + 1
                if idx + 1 == len(s):
                    str = s[sliceStart:len(s) + 1]
                    if (len(str) == k):
                        result.append(str)
                    else:
                        for i in range(len(str), k):
                            str += fill
                        result.append(str)
                    sliceStart = len(s)
        return result

solution = Solution()
testCase = "hjefcvizjkecrioqhyw"
print(solution.divideString(testCase, 3, 'x'))