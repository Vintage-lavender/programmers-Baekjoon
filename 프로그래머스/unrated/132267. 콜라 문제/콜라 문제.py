def solution(a, b, n):
    answer = 0
    while n>=a:
        spare = n%a 
        full = (n//a) * b
        answer += full
        print(n,answer)
        n = (full+spare)
    return answer