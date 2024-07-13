#!/usr/bin/python3
def minOperations(n):
    if n == 1:
        return 0
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n + 1
        operations += 1
    return operations + 1
