#HW1 Q2(b) confirm the affine cipher

# find a^-1 for a
def inverse(a):
    for i in range(0,26):
        if ((a*i) % 26) == 1:
            return i
    return False
        

def Confirm():
    test = True
    # test for all x,y,a,b,a^-1 in the set z/26
    for a in range(0,26):
        # exclude the case for no a^-1
        if inverse(a) != False:
            for b in range(0,26):
                for x in range(0,26):
                    y = ((a*x) + b) % 26
                    #check for the case a=7, b=18, and y=13 or x=3
                    if a==7 and b==18 and (y==13 or x==3):
                        print('y = ',y,', x = ',x,' for a=7, b=18')
                    #test if x equal to the formula if a^-1 exist
                    if x != (inverse(a)*(y-b)) % 26:
                        test = False
                        return test
    return test

print(Confirm())
                
