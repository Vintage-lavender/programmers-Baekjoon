def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion+[None]):
        if p!=c:
            return p