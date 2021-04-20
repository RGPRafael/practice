def alternatingCharacters(s):
    new_string = list()
    deletion = 0
    for i in s: new_string.append(i)
    for i in range( len(new_string) - 1 ) :
        if new_string[i] != new_string[i+1]: continue
        else : deletion += 1
    return deletion

q = int(input())
for q_itr in range(q):
    s = input()
    result = alternatingCharacters(s)
    print(result)