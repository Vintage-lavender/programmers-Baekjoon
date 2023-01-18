def solution(a, b):
    if a>b: 
        a,b = b,a
    return sum(range(a,b+1))
    #return sum(range(min(a,b),max(a,b)+1))
