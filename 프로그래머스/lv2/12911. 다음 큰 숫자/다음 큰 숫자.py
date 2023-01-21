
def solution(n):
    '''
    #뒤에서부터 0의 인덱스 찾기. 0의 인덱스 다음 인덱스의 값이 1일때 자리 교체
    nlist = list(map(str,'0'+bin(n)[2:]))
    #print(nlist)
    for i in range(len(nlist)-1,0,-1):
        if nlist[i]=='1' and nlist[i-1]=='0':
            nlist[i], nlist[i-1] = nlist[i-1], nlist[i]
            nlist[i:] = sorted(nlist[i:])
            return int(''.join(nlist),2)
    '''
    num1 = bin(n).count('1') #이진수의 1개수 세기
    while True:
        n +=1 #1씩 늘려가며 n보다 큰 수 중에서 이진수의 1개수가 n과 같은 것 찾기
        if num1 == bin(n).count('1'): #갱신된 n의 1개수
            break
    return n
    
        