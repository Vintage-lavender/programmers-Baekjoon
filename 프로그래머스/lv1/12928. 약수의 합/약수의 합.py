def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n == i*(n//i):
            answer += (i+n//i)
            if i**2 == n:
                answer -= i
    return answer