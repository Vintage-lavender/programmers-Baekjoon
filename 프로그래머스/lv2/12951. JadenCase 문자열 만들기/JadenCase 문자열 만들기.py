def solution(s):
    # s.lower().title()은 숫자 뒤에 나오는 문자까지 대문자로 만드므로 사용 어려움
    #문자열 길이가 2 이상이면 인덱스1 사용 가능, 문자열 길이 1이하면 그 문자 자체를 대문자로 쓰면 됨
    return ' '.join(list(map(lambda x: x[0].upper()+x[1:].lower() if len(x)>=2 else x.upper(),s.split(' '))))