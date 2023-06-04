#HW1 question 2(a)
count = 0
#for all a, find the a*a^-1 mod 26 = 1
for a in range(0,26):
    for i in range(0,26):
        if ((a*i) % 26) == 1:
            print('a=', a ,', a^-1=', i)
            count+=1
print(count)