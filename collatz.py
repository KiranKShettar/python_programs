def collatz(num):
        if num % 2 == 0:
            result = num // 2
        else:
            result =  3 * num + 1
        print(result, end=' ')
        return result 
try:
    num = int(input("Enter a number: "))     
    print(num, end=' ')
    while num != 1:
        num = collatz(num)
         
except ValueError:
    print("Please enter a valid integer.")