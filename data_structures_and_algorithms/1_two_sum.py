class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_dict = {}
        for idx, num in enumerate(nums):
            val = target - num
            if val in number_dict.keys():
                return [idx, number_dict[val]]
            else:
                number_dict[num] = idx

        

solution = Solution()
testCase = [2,7,11,15]
print(solution.twoSum(testCase, 9))