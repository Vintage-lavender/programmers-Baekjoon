#두 타일 개수를 모두 더한게 전체 타일 개수
#전체 타일 개수로 직사각형을 만들고 그 안에서 노란색 직사각형을 만들되 
#노란색 직사각형의 세로와 가로는 전체 직사각형의 세로와 가로보다 1씩 작아야 함
#즉, 전체 크기가 (n*m)이면 노란 부분은 ((n-2)*(m-2))면 된다
#가로길이 >= 세로 길이(긴 길이 먼저 출력되게 함)
def solution(brown, yellow):
    total = brown + yellow
    for h in range(3,int(total**0.5)+1): #세로 길이만 탐색
        if total%h == 0:
            w = total//h
            if (w-2)*(h-2) == yellow:
                return [w,h]
           
