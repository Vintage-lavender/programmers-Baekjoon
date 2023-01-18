def solution(s):
    ilen = (len(s)-1)
    return s[ilen//2] if len(s)%2 else s[ilen//2:ilen//2+2]