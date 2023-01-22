#앞의 두 수를 비교하면서 최소공배수를 갱신
def gcd(a,b): #a>=b
    print(a,b)
    if b%a==0:
        return a
    return gcd(b%a,a)
    '''
    a,b = min(a,b), max(a,b)
    maximum = 1
    for i in range(1,int(a**0.5)+1):
        if a%i==0:
            if b%i==0:
                maximum = i
            if b%(a//i)==0:
                return (a*b)//(a//i)
    return (a*b)//maximum
    '''

def solution(arr):
    arr.sort()
    x = arr[0]
    for i in range(1,len(arr)):
        x,y = min(x,arr[i]), max(x,arr[i])
        x = (x*y)//gcd(x,y)
    return x