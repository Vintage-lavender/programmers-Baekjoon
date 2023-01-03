def solution(babbling):  
    a = ["aya", "ye", "woo", "ma" ]
    answer = 0
    for l in babbling:
        start = 0
        end = 0
        while end<len(l):
            end += 1
            if l[start:end] in a:
                if end<len(l) and l[start]==l[end]:
                    break
                start = end
        if start == end:
            answer += 1
    return answer