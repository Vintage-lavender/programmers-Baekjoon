#2의 지수승으로 나눴을 때 몫이 같아지는 순간!
def solution(n,a,b):
    import math
    n = int(math.log(n,2))
    a -= 1
    b -= 1
    for i in range(n+1):
        if a//(2**i)==b//(2**i):
            return i