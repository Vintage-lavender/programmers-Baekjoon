#주는 학생에게 우선 순위가 있으므로 주는 학생의 입장에서 생각하기.
#갖고 온 애가 잃어버릴 경우 빌려 줄 수가 없음
def solution(n, lost, reserve):
    answer = n #모든 학생이 입는 경우 가정
    stud = [0 for _ in range(n+2)] #모든 학생이 체육복을 가져왔고, 여벌 체육복은 없다고 가정
    
    for l in lost:
        stud[l] -= 1
        answer -= 1 #모든 잃어버린 학생들이 못입는 경우 가정
    
    for r in sorted(reserve): #남은 학생 중 가장 작은 학생 --> 남은 학생 중 가장 작은 학생
        stud[r] += 1
        
        if stud[r] == 0: #분실하고 앞의 학생한테 옷을 못 받은 경우
            answer += 1 #자급자족
            
        elif stud[r] == 2:#분실하고 앞의 학생에게 옷을 받은 경우
            stud[r] = 0 #자급자족
            #answer는 증가시켜줬으므로 증가 생략
        
        if stud[r]==1: #분실하지 않은 경우(다른 학생에게 옷을 줄 수 있는 경우)
            answer += 1 #무조건 주는 경우 가정
            if stud[r-1] == -1: #앞 학생이 분실한 경우
                stud[r-1] += 1 #굳이 값을 바꿀 필요는 없어 보임
            elif stud[r+1] == -1: #뒤 학생이 분실한 경우
                stud[r+1] += 2 #뒤 학생에게 옷을 줌
            else: #앞뒤에 분실한 학생이 없을 경우
                answer -= 1
        
        #print(r,answer)
    
    return answer