
#Fibonacci
#1,1,2,3,5,8,13,21,34,55,89...
cnt = 0

def fib(n):
    global cnt
    cnt += 1
    print(f"{cnt}: {n}")
    if n <= 2:
        return 1
    
    return fib(n-1)+fib(n-2)

fib(5)