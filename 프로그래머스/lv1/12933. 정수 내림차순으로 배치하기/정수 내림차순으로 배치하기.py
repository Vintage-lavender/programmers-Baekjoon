def solution(n):
    return int(''.join(sorted(map(str,str(n)),reverse=True)))