#모든 숫자를 2진수로 바꿔줌
def solution(n, arr1, arr2):
    answer = []
    for a1,a2 in zip(arr1,arr2):
        str1 = ''
        str2 = ''
        i = 2**n
        while i%2==0:
            i //= 2
            str1 += str(a1//i)
            str2 += str(a2//i)
            a1 -= i * (a1//i)
            a2 -= i * (a2//i)
        a = ''
        for s1,s2 in zip(str1,str2):
            if int(s1) or int(s2):
                a += '#'
            else:
                a += ' '
        answer.append(a)
    return answer