def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range((i+1),(len(nums)-1)):
            for k in range((j+1),len(nums)):
                comb = nums[i]+nums[j]+nums[k]
                n = 2
                while comb%n:
                    n+=1
                if comb==n:
                    answer += 1
    return answer