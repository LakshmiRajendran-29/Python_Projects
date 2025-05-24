# 7. Check if a number is prime

def isPrime(n):
    if n <=1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n % i ==0:
            print(i)
            return False
    return True

num =123
if isPrime(num):
    print(f'{num} is a Prime Number')
else:
    print(f'{num} is not a Prime Number')
