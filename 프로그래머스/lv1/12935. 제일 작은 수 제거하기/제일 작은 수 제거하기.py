def solution(arr):
    minvalue = min(arr)
    return [i for i in arr if i!=minvalue] or [-1]