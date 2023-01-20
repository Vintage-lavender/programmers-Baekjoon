#작은 것의 약수 구하고, 큰 것의 배수구하기(n*m에서 n의 크기 줄여가면서 배수 확인)
def solution(n, m):
    answer = []
    if n>m:
        n,m = m,n
    #n의 약수 구하기
    largest = 1
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if m%(n//i)==0:
                largest = n//i
                break
            elif m%i==0:
                largest = i
    
    #smallest = m
    #while smallest <= n*m:
    #    if (smallest%n)==0:
    #        break
    #    else:
    #        smallest += m
          
    return [largest,n*m/largest]