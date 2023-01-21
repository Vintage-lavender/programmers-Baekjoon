def solution(s):
    cnt = 0
    zlen = 0
    while s!='1':
        #new = len(s.replace('0',''))
        new = s.count('1')
        zlen += len(s) - new
        s = bin(new)[2:]
        cnt += 1
    return [cnt,zlen] #변환횟수, 제거된 0개수