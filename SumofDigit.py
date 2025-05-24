# Sum of Digits Using while loop

num = 12345
count = 0

while num > 0 :
    digit = num%10
    count+=digit
    num = num//10
print(count)
