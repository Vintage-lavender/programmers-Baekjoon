def solution(food_times, k):
    answer = 0

    while k > 0 :
        
        foods = len(food_times) #남은 음식 수
        
        empty_foods = food_times.count(0) #다 먹은 음식 수
        
        a = k // (foods - empty_foods) # 모든 음식의 양이 충분할 때, 낱개 음식에서 섭취할 수 있는 시간
        b = k % (foods - empty_foods) # 남은 시간

        for i, j in zip(food_times, range(foods)): #매번 입력받은 모든 원소 n을 순회하는 반복문
            
            if food_times[j] != 0: #다먹지 않은 음식일 경우
                
                food_times[j] = i - a # 현재 음식에 남은 섭취시간 - 낱개 음식 섭취 시간
                
                if food_times[j] < 0: # 현재 음식에 남은 섭취시간이 a 시간보다 남은 시간이 부족했을 경우
                    
                    b = b - food_times[j] # 부족했던 시간을 남은 시간에 더해주기
                    
                    food_times[j] = 0 # 현재 음식 남은 양 0으로 갱신
            k = b # 남은 시간 갱신

        if foods - food_times.count(0) ==0: # 주어진 시간 k 내에 모두 다먹은 경우
            return -1

        if k+1 <= len(food_times) - food_times.count(0):
            for i in food_times:
                answer += 1
                if i !=0 :
                    k -= 1
                if k == -1:
                    return answer