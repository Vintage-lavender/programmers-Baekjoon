#이전에 나온 단어, 직전단어의 끝과 같지 않은걸로 시작하는 단어, 한글자 단어 등장(입력조건 아님)시 탈락발생
def solution(n, words):
    answer = []
    cnt = 0
    wset = set(words)
    for i,w in enumerate(words):
        if i%n==0:
            cnt += 1
        if w in wset:
            wset -= {w}
            if i and words[i-1][-1]!=w[0] : 
                return [i%n+1,cnt]
        else:
            return [i%n+1,cnt]
        #print(wset)
    return [0,0] #가장 먼저 탈락하는 사람의 번호, 몇번째차례에 탈락하는지