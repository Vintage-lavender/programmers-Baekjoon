import re
def solution(s):
    #return len(re.sub('\D',"",s)) == len(s) and (len(s) in [4,6]) #문자(\D)빼고 정수만 남기기
    return s.isdigit() and (len(s) in [4,6])