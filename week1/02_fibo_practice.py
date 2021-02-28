input = 10

def fibo_recursion(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1

    return fibo_recursion(n-1) + fibo_recursion(n-2)

for i in range(1,input):
    print(fibo_recursion(i))