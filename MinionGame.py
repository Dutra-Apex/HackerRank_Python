def minion_game(string):
    
    p1 = 0
    p2 = 0
    
    for i in range(len(string)):
        if s[i] in "AEIOU":
            p1 += (len(string)) - i
        else:
            p2 += (len(string)) - i
            
    if p1 > p2:
        print("Kevin", p1)
    elif p1 < p2:
        print("Stuart", p2)
    else :
        print("Draw")
