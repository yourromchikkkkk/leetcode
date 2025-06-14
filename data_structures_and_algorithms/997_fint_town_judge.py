from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1: 
            return 1
        counterMap = [0] * (n + 1)
        for person in trust:
            counterMap[person[0]] -= 1
            counterMap[person[1]] += 1
        for idx, count in enumerate(counterMap):
            if count == n - 1:
                return idx
        return -1


n = 2
testCase = [[1,2]]
solution = Solution()
print(solution.findJudge(n=n, trust=testCase))