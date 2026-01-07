from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tempMap = dict()

        for idx in range(len(numbers)):
            needed = target - numbers[idx]
            if needed in tempMap:
                return [tempMap[needed] + 1, idx + 1]
            tempMap[numbers[idx]] = idx

solution = Solution()
testCase = [2,7,11,15]
target = 13
print(solution.twoSum(testCase, target)) # [1, 3]