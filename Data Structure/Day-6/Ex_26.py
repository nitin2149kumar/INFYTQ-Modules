#DSA-exer-26

import sys

sys.setrecursionlimit(10000)   #This is to overcome default python recursion limit

def fibonacci(num):
    #Remove pass and write your logic here
    if num in memo.keys():
        return memo[num]
    elif num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

memo={} #global dictionary to store the fibonacci number already computed
print("Fibonacci number:",fibonacci(6))
