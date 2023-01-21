#가운데 있는 수가 약수임
#홀수인 약수 개수
def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if i%2:
                answer += 1
            if n!=i**2 and (n//i)%2:
                answer += 1
    return answer