#가운데 있는 수가 약수임
#홀수인 약수 개수
def solution(n):
    answer = 0
    #홀수만 보면 되니까
    #for i in range(1,int(n**0.5)+1,2):
    #이렇게 생각했으나 짝수의 경우 26= 2 x 13 이렇게 나눠져있을 수 있으므로 모든 홀수 약수를 구하려면 정직하게 다 보아야 함..ㅎㅎ
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if i%2:
                answer += 1
            if n!=i**2 and (n//i)%2:
                answer += 1
    return answer