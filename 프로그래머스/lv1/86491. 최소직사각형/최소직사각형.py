def solution(sizes):
    #가로를 더 길게 만드는 걸로 가정
    wmax = 0
    hmax = 0
    for w,h in sizes:
        if w<h:
            w,h = h,w
        wmax = max(wmax,w)
        hmax = max(hmax,h)
    answer = wmax * hmax
    return answer