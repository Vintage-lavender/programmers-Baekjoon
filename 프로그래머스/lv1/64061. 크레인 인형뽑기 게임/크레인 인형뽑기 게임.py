def solution(board, moves):
    answer = 0
    blen = len(board)
    #열의 제일 상위 위치를 알려주는 리스트 생성
    top = [blen+1] * (blen+1) #알고리즘을 효율적으로 작동시키기 위해 원소와 원소개수 모두 blen+1
    
    stack = [0]
    for m in moves:
        if top[m] == (blen+1): #최상위를 아직 찾지 않았을 때
            for i in range(len(board)): #입력된 열의 최상위만 찾는것이 효율적
                if board[i][m-1] != 0:
                    top[m] = i
                    break 
        if top[m] < blen:
            if stack[-1] == board[top[m]][m-1]:
                answer += 2
                stack.pop()
            else:
                stack.append(board[top[m]][m-1])
            top[m] += 1

    return answer