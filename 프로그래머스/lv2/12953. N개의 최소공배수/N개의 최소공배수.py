#앞의 두 수를 비교하면서 최소공배수를 갱신
def lcm(a,b):
    a,b = min(a,b), max(a,b)
    maximum = 1
    for i in range(1,int(a**0.5)+1):
        if a%i==0:
            if b%i==0:
                maximum = i
            if b%(a//i)==0:
                return (a*b)//(a//i)
    return (a*b)//maximum

def solution(arr):
    arr.sort()
    l = arr[0]
    for i in range(1,len(arr)):
        l = lcm(l,arr[i])
    return l