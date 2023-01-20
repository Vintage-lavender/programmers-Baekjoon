def solution(s):
    return ' '.join(list(map(lambda x: x[0].upper()+x[1:].lower() if len(x)>=2 else x.upper(),s.split(' '))))