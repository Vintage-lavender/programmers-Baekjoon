import re
def solution(new_id):
    new_id = new_id.lower()
    #sym = re.compile('[a-z 0-9 -_.]') #보관할 것
    #new_id = ''.join(sym.findall(new_id)).split('.')
    new_id = re.sub('[^a-z0-9-_.]','',new_id).split('.')
    answer = ''
    for i in new_id:
        if i:
            answer += i+'.'
    new_id = answer.rstrip('.')
    
    print(new_id)
    
    if not new_id:
        new_id += 'aaa'
    elif len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    elif len(new_id) <= 2:
        while len(new_id)<3:
            new_id += new_id[-1]
    

    return new_id