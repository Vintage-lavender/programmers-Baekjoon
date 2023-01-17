def solution(participant, completion):
    participant.sort()
    completion = sorted(completion) + [None]
    for p,c in zip(participant,completion):
        if p!=c:
            return p