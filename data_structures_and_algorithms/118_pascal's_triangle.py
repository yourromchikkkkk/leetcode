from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows >= 1:
            result.append([1])
        if numRows > 1:
            result.append([1,1])
        for row in range(2, numRows):
            print(row)
            rowArray = [1] * (row + 1)
            previousRow = result[len(result) - 1]
            for elementIdx in range(1, len(rowArray) - 1):
                rowArray[elementIdx] = previousRow[elementIdx - 1] + previousRow[elementIdx]
            result.append(rowArray)
        return result
            
solution = Solution()
testCase = 5
print(solution.generate(testCase))