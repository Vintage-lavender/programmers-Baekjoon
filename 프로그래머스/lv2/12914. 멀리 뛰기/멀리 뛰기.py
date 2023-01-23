def solution(n):
    '''
    dp = [1]*(n+1)
    for i in range(2,n+1):
        dp[i] = dp[i-2]+dp[i-1]
    return dp[n]%1234567
    '''
    #print(40)
    a,b = 1,1
    #print(a,b)
    #while b<n: #n이 커지면 경우의 수가 n보다 커지는 것은 매우 당연하므로 이 코드는 틀렸음
    for i in range(n-1):
        a,b = b,(a+b)
        #print(a,b)
    return b%1234567
    