#뒤에서부터 0의 인덱스 찾기. 0의 인덱스 다음 인덱스의 값이 1일때 자리 교체
def solution(n):
    nlist = list(map(str,'0'+bin(n)[2:]))
    #print(nlist)
    for i in range(len(nlist)-1,0,-1):
        if nlist[i]=='1' and nlist[i-1]=='0':
            nlist[i], nlist[i-1] = nlist[i-1], nlist[i]
            nlist[i:] = sorted(nlist[i:])
            return int(''.join(nlist),2)
    
        