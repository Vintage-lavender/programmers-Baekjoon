#모든 달은 28일까지 있다고 가정

def solution(today, terms, privacies):
    tdict = {}
    answer = []
    year,month,day = map(int,today.split('.'))
    for t in terms:
        a,n = t.split(' ')
        tdict[a] = int(n)
    for i,p in enumerate(privacies):
        date,a = p.split(' ')
        y,m,d = map(int,date.split('.'))
        print(i, y,m,d)
        m += tdict[a] #12월까지를 보장해야함
        y += m//12
        if m%12==0:
            y-=1
            m = 12
        else:
            m = m%12
        if d ==1:
            d = 28
            if m==1:
                m=12
            else:
                m-=1
        else:
            d -= 1
        print(" ", y,m,d)
        if y>=year:
            if m>=month:
                if y==year and m==month and d<day:
                    answer.append(i+1)
            elif y==year:
                answer.append(i+1)
        else:
            answer.append(i+1)

    return answer