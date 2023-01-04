def solution(N, stages):
    answer = [] #단계별로 (단계, 실패율)로 저장
    slist = [0] * 502 #전체가 500단계인 경우 slist[501]에도 값이 할당될 수 있음
    for s in stages:
        slist[s] += 1
    people = len(stages) #남은 사람 수
    for i in range(1,N+1):
        p = 0
        if people != 0:
            p = slist[i]/people
        answer.append((i,p))
        people -= slist[i] #남은 사람 수 갱신
    #단계순으로 리스트에 삽입했으므로 단계별로 오름차순 정렬이 이미 되어 있음.
    #실패율이 큰 것 부터 내림차순 정렬 후 단계만 출력
    return list(map(lambda x: x[0] ,sorted(answer, key=lambda x: x[1], reverse=True)))
