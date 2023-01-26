#n: citation 길이
#h: 인용횟수
#h이상 인용된 논문은 h≤개, h이하 인용된 논문은 h≥개
def solution(citations):
    citations.sort()
    papers = len(citations)
    for i,c in enumerate(citations): #최댓값, h값의 경계는 인용횟수 중에서 결정됨.
        if c >= papers-i: #인덱스를 그대로 빼주면 c이하로 인용된 논문을 빼고 셀 수 있음.
            return papers-i
    return 0 #h값을 찾지 못한 경우 h=0

    
    '''
    answer = 0
    #인용횟수 리스트
    cnt = [0] * 10001
    for i in citations:
        cnt[i] += 1
    start = 0
    end = max(citations)
    while start<=end:
        mid = (start+end)//2
        hlow = sum(cnt[:mid])
        hhigh = sum(cnt[mid:])
        if hlow<=mid and hhigh>=mid:
            answer = mid
            start = mid+1
        else:
            end = mid-1'''
    return answer