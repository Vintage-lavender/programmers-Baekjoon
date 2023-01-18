def solution(arr, divisor):
    answer = []
    arr.sort()
    for a in arr:
        if a%divisor==0:
            answer.append(a)
    return answer or [-1]