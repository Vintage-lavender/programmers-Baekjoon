def solution(n):
    #print(sorted(str(n))) #sorted에 스트링을 그대로 넣으면 모든 문자가 정렬됨
    #리스트에 스트링을 그대로 넣으면 문자한개씩 분리됨 list(str(n))
    return int(''.join(sorted(map(str,str(n)),reverse=True)))