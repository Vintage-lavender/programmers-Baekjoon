def solution(n):
    fibo = [0] * (n+1)
    fibo[1] = 1
    i = 2
    while i<=n:
        fibo[i] = fibo[i-1]+fibo[i-2]
        i+=1
    return fibo[n]%1234567