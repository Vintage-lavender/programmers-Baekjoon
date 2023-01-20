def solution(n):
    num=set(range(2,n+1))
    for i in range(2,n+1):
        if i in num: #이전 차집합 과정을 거친 후에도 남아있는 수에 대하여만 수행
            num-=set(range(2*i,n+1,i)) #i의 배수를 모두 빼줌
    return len(num)
'''
    answer = 1
    for i in range(3,n+1):
        cnt = 0
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                cnt += 1
                break
        if cnt==0:
            answer += 1
    return answer
'''