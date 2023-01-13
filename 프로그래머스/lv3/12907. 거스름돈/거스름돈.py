#있는 단위로 n을 구성하는 경우의 수
#순서를 고려하지 않으므로 오류가 남
#2차원 리스트 생성
def solution(n, money):
    answer = 0
    dp = [0] * (n+1)
    for m in money:
        for price in range(m,n+1):
            if price == m:
                dp[price] += 1
            else:
                dp[price] += dp[price-m]
        
    return dp[n]