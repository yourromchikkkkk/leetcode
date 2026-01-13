from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            left, right = idx + 1, len(nums) - 1

            while left < right and right < len(nums):
                treeSum = val + nums[left] + nums[right]
                if treeSum > 0:
                    right -= 1
                if treeSum < 0:
                    left += 1
                if treeSum == 0:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return res
        
sol = Solution()
testCase = [-1,0,1,2,-1,-4]
print(sol.threeSum(testCase))