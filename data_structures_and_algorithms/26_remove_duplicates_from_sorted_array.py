from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j, i = 1, 1

        while i <= len(nums) - 1 and j <= len(nums) - 1:
            if nums[i - 1] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1

        
        return i
    

solution = Solution()
testCase = [0,0,1,1,1,2,2,3,3,4]
print(solution.removeDuplicates(testCase))
