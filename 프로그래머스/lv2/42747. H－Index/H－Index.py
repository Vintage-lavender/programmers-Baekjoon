#n: citation 길이
#h: 인용횟수
#h이상 인용된 논문은 h≤개, h이하 인용된 논문은 h≥개
def solution(citations):
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
            end = mid-1
    return answer