def solution(s):
    
    '''
    #첫번째 방법
    try:
        int(s)
        return len(s) in [4,6]
    except:
        return False
    '''
    '''
    #두번째 방법
    import re
    return len(re.sub('\D',"",s)) == len(s) and (len(s) in [4,6]) #문자(\D)빼고 정수만 남기기
    '''
    #가장 시간이 적게 걸리는 세번째 방법
    return s.isdigit() and (len(s) in [4,6])
