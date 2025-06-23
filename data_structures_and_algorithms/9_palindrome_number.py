class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        temp = x
        while temp != 0:
            reverse = (reverse * 10) + (temp % 10)
            temp = temp // 10
        return (reverse == x)
    
solution = Solution()
print(solution.isPalindrome(1223221))