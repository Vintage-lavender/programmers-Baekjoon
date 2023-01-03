def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if int(n**0.5)**2 == n: #루트 씌워주고 제곱한 값이 n과 같으면
            answer -= n*2
        answer += n
    return answer