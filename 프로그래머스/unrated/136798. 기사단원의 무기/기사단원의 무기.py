def solution(number, limit, power):
    answer = 0
    dlist = [0] * (number+1)
    for i in range(1,number+1):
        a = []
        num = 0
        for j in range(1,int(i**0.5)+1):
            if i%j == 0:
                a.append(i//j)
                a.append(j)
                if dlist[i//j] >= limit:
                    num = limit+1
                    break
        if num == 0:
            num = len(set(a))
        dlist.append(num)
        answer += num if num<=limit else power
    return answer