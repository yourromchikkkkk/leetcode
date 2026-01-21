from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        left, right = 0, 1

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                maxP = max(maxP, prices[right] - prices[left])
            right += 1
        
        return maxP

solution = Solution()
testCase1 = [7,1,5,3,6,4] # 5
testCase2 = [7,6,4,3,1] # 0
testCase3 = [2,1,2,1,0,1,2] # 2
testCase4 = [5,1,5,6,7,1,10] # 9

# print(solution.maxProfit(testCase1))
# print(solution.maxProfit(testCase2))
# print(solution.maxProfit(testCase3))
print(solution.maxProfit(testCase4))