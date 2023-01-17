#모든 숫자를 2진수로 바꿔줌
def solution(n, arr1, arr2):
    answer = []
    for a1,a2 in zip(arr1,arr2):
        row = bin(a1|a2)[2:].rjust(n,'0')
        row = row.replace('1','#')
        row = row.replace('0',' ')
        answer.append(row)
    return answer