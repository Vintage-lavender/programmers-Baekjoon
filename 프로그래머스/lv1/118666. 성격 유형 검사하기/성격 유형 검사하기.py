def solution(survey, choices):
    answer = ''
    klist = {'TR':0,'FC':0,'MJ':0,'NA':0}
    for s in range(len(survey)):
        #print(klist)
        for k in klist:
            if survey[s] == k:
                klist[k] += choices[s] - 4
                break
            elif survey[s][0] == k[1]:
                klist[k] += -(choices[s] -4)
                break
    #print(klist)
    for k in klist:
        if klist[k]<0:
            answer += k[0]
        else:
            answer += k[1]
    return answer