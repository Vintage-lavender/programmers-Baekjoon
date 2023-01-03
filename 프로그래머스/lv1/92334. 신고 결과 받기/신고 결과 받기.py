def solution(id_list, report, k):
    mail = {id:0 for id in id_list} 
    block = {id:[] for id in id_list} 
    for r in report:
        s, e = r.split()
        block[e].append(s)
    for id in id_list: 
        real = set(block[id])
        if len(real) >=k:
            for i in real:
                mail[i] += 1
    answer = []
    for i in mail:
        answer.append(mail[i])
    
    return answer