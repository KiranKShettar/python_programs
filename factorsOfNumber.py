n = 10
result = []

class Solution:
    def factorOf(self,n):
        for i in range(1,n+1):
            if n % i ==0:
                result.append(i)
        return result
    
sol = Solution()
print(sol.factorOf(n))