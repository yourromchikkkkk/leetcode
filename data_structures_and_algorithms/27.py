class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        startP, endP = 0, len(nums) - 1

        while startP <= endP:
            if nums[startP] == val:
                nums[startP] = nums[endP]
                endP -= 1
            else: 
                startP += 1
        return startP

        
    

solution = Solution()
testCase = [1]
# testCase = [0,1,2,2,3,0,4,2]
print(solution.removeElement(testCase, 1))
print(testCase)