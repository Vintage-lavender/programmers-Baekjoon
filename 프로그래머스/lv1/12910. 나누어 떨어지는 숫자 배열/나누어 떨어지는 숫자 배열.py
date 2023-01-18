def solution(arr, divisor):
    answer = []
    arr.sort()
    for a in arr:
        if a%divisor==0:
            answer.append(a)
    if not answer:
        answer = [-1]
    return answer