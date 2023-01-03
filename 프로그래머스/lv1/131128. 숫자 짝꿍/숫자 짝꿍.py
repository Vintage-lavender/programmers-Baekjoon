def solution(X, Y):
    answer =''
    numlist = []
    xlist = [0] * 10
    ylist = [0] * 10
    for x in X:
        x = int(x)
        xlist[x] += 1
    for y in Y:
        y = int(y)
        ylist[y] += 1
    for i in range(10):
        numlist+= [i]*min(xlist[i],ylist[i]) 

    if len(numlist) == 0:
        return '-1'
    elif sum(numlist) == 0:
        return '0'
    numlist.sort(reverse=True)
    for i in numlist:
        answer += str(i)

    return answer