#순간이동은 건전지가 닳지 않음
#시작위치는 0
#5000 = 2**3 * 5**4
def solution(n):
    '''
    #dp: 최소 경우의 수를 기록
    dp = [0]*(n+1)
    for i in range(1,n+1):
        dp[i] = dp[i-1]+1
        if i%2==0: #직전에서 오는게 최소인지 2나눈것에서 오는게 최소인지 비교
            dp[i] = min(dp[i],dp[i//2])
    return dp[n] #런타임에러/시간초과 원인: n의 크기
    '''
    answer = 1
    while n!=1: #2로 나눠주다가 홀수 되면 1빼주고 2나누고를 반복하기
        if n%2==0:
            n//=2
        else:
            n-=1
            answer +=1
    return answer #2가 아닌 서로소를 2의 제곱으로 만들기 위해 빼야하는 1의 개수+1