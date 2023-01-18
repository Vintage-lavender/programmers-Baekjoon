def solution(arr):
    #minvalue = min(arr)
    #return [i for i in arr if i!=minvalue] or [-1]
    arr.remove(min(arr))
    return arr or [-1]