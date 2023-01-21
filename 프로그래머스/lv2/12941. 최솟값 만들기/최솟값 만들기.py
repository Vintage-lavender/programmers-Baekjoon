def solution(A,B):
    #return sum(map(lambda x: x[0]*x[1],zip(sorted(A),sorted(B,reverse=True))))
    #return sum(map(lambda a,b : a*b, sorted(A), sorted(B, reverse=True)))
    return sum(a*b for a,b in zip(sorted(A), sorted(B, reverse=True)))