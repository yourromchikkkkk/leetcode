class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
            
        firstPrev = 1
        secondPrev = 2
        current = firstPrev + secondPrev

        for idx in range(3, n):
            firstPrev = secondPrev
            secondPrev = current
            current = firstPrev + secondPrev
        return current