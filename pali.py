__author__ = 'rfischer'

N = input()

for x in range(0, N):
    T = raw_input()
    n = len(T) / 2

    sum = 0
    for y in range(0, n):
        sum += abs(ord(T[y]) - ord(T[-(y+1)]))
    print sum
