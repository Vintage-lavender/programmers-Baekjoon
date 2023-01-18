def solution(arr, divisor):
    answer = []
    arr.sort()
    for a in arr:
        if a%divisor==0:
            answer.append(a)
        elif arr[-1] == a and len(answer)==0:
            answer = [-1]
    return answer