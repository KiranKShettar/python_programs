n = 153 
class Solution():
    def checkArmstrongNumber(self,n):
        num = n
        total = 0
        power =  len(str(n))

        while num > 0:
            id = num % 10
            total = total + (id ** power)
            num = num // 10
        return total == n

sol = Solution()
print(sol.checkArmstrongNumber(n))