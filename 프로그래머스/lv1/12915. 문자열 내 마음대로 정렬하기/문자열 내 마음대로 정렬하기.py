#9분
#사전순으로 단어 배열 후 n번째 인덱스에 따라 단어 배열
def solution(strings, n):
    strings.sort()
    return sorted(strings,key=lambda x: x[n])
