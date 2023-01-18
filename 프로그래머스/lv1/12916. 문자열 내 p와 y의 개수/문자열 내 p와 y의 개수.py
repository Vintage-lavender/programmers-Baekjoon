from collections import Counter
def solution(s):
    answer = True
    s = s.lower()
    c = Counter(s)
    if c['p']==c['y']:
        return answer
    return not answer