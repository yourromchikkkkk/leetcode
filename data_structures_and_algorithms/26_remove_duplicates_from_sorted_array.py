from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowP, fastP = 1, 1

        while fastP < len(nums): 
            if nums[fastP] != nums[slowP - 1]:
                nums[slowP] = nums[fastP]
                slowP += 1
            fastP += 1
        return slowP


solution = Solution()
testCase = [0, 0, 1, 1, 1, 2, 2, 3, 4]
print(solution.removeDuplicates(testCase))
print(testCase)