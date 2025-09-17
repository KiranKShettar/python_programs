x = 121
class Solution:

    def isPalindrome(self,x):

        if x < 0:
            return False
        
        original = x
        result = 0 

        while x > 0:
            id = x % 10
            x = x // 10
            result = result*10 + id

        return result == original


sol = Solution()
print(sol.isPalindrome(x))