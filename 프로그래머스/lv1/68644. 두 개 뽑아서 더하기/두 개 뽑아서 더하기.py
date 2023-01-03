def solution(numbers):
    answer = []
    for i in range(len(numbers)-1): #-1을 해주지 않더라도 제일 마지막엔 아래의 반복문이 작동하지 않음
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer))) #set이후 정렬을 해야 리스트의 원소들이 정렬됨