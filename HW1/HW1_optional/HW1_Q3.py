from math import factorial

#calculate the nCr
def binomial_coefficients(n,r):
    C = factorial(n)/(factorial(r)*factorial(n-r))
    return int(C)

line = int(input('input the number of lines: '))

i = 0
x = []
while i < line:
    tmp = []
    #change the data type to str and store it to tmp, then join the data tgt for each line with spacing
    for j in range(i+1):
       tmp.append(str(binomial_coefficients(i, j)))
    tmp2 = '   '.join(tmp)
    #store each line to a list
    x.append(tmp2)
    i+=1
max_len = len(x[-1])

#print out each line with space int((max_len - len(x[i]))/2)
for i in range(line):
    space = int((max_len - len(x[i]))/2)
    print(space*' ', x[i])



