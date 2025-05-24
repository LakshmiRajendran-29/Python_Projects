
# 6. Fibonacci series up to n terms
n=7
a=0
b=1
print(a)
print(b)
i=2
while i < n:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
