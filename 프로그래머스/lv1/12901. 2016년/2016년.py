def solution(a, b):
    answer = ''
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    last = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day[(sum(last[0:(a-1)])+b-1)%7]