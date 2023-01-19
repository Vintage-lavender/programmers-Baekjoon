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
    return answer[:-1]