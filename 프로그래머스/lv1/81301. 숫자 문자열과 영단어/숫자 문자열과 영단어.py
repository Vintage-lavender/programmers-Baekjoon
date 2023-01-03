def solution(s):
    answer = ''
    word = ['zero','one','two','three','four','five','six','seven','eight','nine']
    i = 0
    while i<len(s):
        tmp = ''
        for w in range(len(word)):
            if s[i:i+2] == word[w][0:2]: #첫 두글자가 같은 경우
                tmp += str(w)
                i += len(word[w])
                break
        if len(tmp) == 0:
            tmp = s[i]
            i += 1
        answer += tmp
    return int(answer)