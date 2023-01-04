def solution(numbers, hand):
    answer = ''
    dial = {'left':[3,0], 'right':[3,2]}
    nothand = 'left'
    if hand =='left':
        nothand = 'right'
    for n in numbers:
        if n==0:
            n=11
        if n%3 == 0:
            n -= 3
            dial['right'] = [n//3,2]
            answer += 'R'
        elif n%3 == 1:
            dial['left'] = [n//3,0]
            answer += 'L'
        else:
            push=[n//3,1]
            hlen = 0
            nlen = 0
            for p,h,nh in zip(push,dial[hand],dial[nothand]):
                hlen += abs(h-p)
                nlen += abs(nh-p)
            if hlen <= nlen:
                dial[hand] = push
                answer += chr(ord(hand[0])-32)
            else:
                dial[nothand] = push
                answer += chr(ord(nothand[0])-32)
    return answer