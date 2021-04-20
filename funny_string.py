def funnyString(s):
    s1 = list()
    s1_abs = list()
    s2_abs = list()
    for i in s: s1.append(ord(i))
    s2 = s1.copy()
    s2.reverse()
    for i in range(len(s1)- 1):
        s1_abs.append( abs( s1[i] - s1[ i+1 ] ) )
        s2_abs.append( abs( s2[i] - s2[ i+1 ] ) )
      
    for i in range(len(s1_abs)):
        if s1_abs[i] != s2_abs[i] : 
            return "Not Funny"
    
    return "Funny" 

q = int(input())

for q_itr in range(q):
    s = input()
    result = funnyString(s)
    print(result)