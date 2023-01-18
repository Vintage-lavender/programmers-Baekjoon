def solution(n):
    #print(list(str(n)))
    #리스트에 스트링을 그대로 넣으면 문자한개씩 분리됨
    return int(''.join(sorted(map(str,str(n)),reverse=True)))