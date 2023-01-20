def solution(nums):
    cand = []
    for i in range(len(nums)-2):
        for j in range((i+1),(len(nums)-1)):
            for k in range((j+1),len(nums)):
                cand.append(nums[i]+nums[j]+nums[k])
    #print(cand)
    index = 0
    while index<len(cand):
        c = cand[index]
        i = 2
        while c%i:
            i+=1
        #print(c, i)
        if i!=c:
            cand.remove(c)
            continue
        index += 1
    #print(cand)
    return len(cand)