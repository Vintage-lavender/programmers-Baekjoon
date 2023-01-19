def solution(s):

    answer = ''
    slist = s.split(' ')
    for word in slist:
        word = list(word.lower())
        for i,w in enumerate(word):
            if i%2==0:
                #word[i] = chr(ord(w)-32)
                word[i] = w.upper()
        answer+=''.join(word)+ ' '
    s.upper()
    print(s)
    return answer[:-1]
    
    #return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
    #위의 경우 a.lower() 혹은 a.upper()가 리스트의 요소 그 자체로 들어가게 되므로 따로 변수 할당이 필요 없음
