from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        if rowIndex >= 0:
            result.append([1])
        if rowIndex > 0:
            result.append([1,1])
        for rowIdx in range(2, rowIndex + 1):
            rowArray = [1] * (rowIdx + 1)
            previousRow = result[rowIdx - 1]
            for elementIdx in range(1, len(rowArray) - 1):
                rowArray[elementIdx] = previousRow[elementIdx - 1] + previousRow[elementIdx]
            result.append(rowArray)
        return result[rowIndex]
    
solution = Solution()
testCase = 3
print(solution.getRow(testCase))