def solution(arr1, arr2):
    answer = []
    for r1, r2 in zip(arr1, arr2):
        tmp = []
        for c1, c2 in zip(r1, r2):
            tmp.append(c1+c2)
        answer.append(tmp)
    return answer