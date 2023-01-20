#'a'=97~122
#'A'=65~90
#print(chr(122),chr(90))
def solution(s, n):
    answer = ''
    for i in s:
        if i==' ':
            answer += ' '
        elif ((ord(i)+n) >= 123) or (ord(i)<= 90 and (ord(i)+n) > 90):
            answer += chr(ord(i)+n-26)
            #print('2:', (ord(i)+n-26))
        else:
            answer += chr(ord(i)+n)
            #print('3:', ord(i), n)
        
    return answer
