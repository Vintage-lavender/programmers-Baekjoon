def solution(s):
    answer = 0
    i = 0
    while i<len(s):
        if i==(len(s)-1):
            answer += 1
            break
        x = s[i]
        xcnt = 1
        cnt = 0
        for j in range(i+1,len(s)):
            if s[j] == x:
                xcnt += 1
            else:
                cnt += 1
            if xcnt == cnt or j==(len(s)-1):
                i = j+1
                break
        answer += 1
    return answer