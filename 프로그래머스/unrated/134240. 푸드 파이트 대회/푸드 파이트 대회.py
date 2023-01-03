def solution(food):
    answer = '0'
    index = len(food)-1
    for i in range(index,0,-1):
        eat = food[i]//2
        answer = eat*str(i) + answer + eat*str(i)
    return answer