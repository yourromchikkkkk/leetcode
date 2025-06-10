class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for idx in range(len(digits) - 1, -1, -1):
            if(digits[idx] == 9):
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
            if idx == 0:
                return [1] + digits
            
solution = Solution()
case1 = [1,2,3]
print(solution.plusOne(case1))
case2 = [4,3,2,1]
print(solution.plusOne(case2))
case3 = [9]
print(solution.plusOne(case3))