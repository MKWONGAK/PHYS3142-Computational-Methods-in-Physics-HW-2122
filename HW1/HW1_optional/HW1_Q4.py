x = [14,46,43,27,57,41,45,21,70]
size = len(x)
tmp =[]
for i in range(size):
    #x[0] wont move at beginning
    if i == 0:
        tmp.append(x[i])
    #compare the x[i] to tmp[j], and count the step needed for moving
    #element in tmp should be in increasing order all the time
    else:
        count = 0
        for j in range(i):
            if x[i] < tmp[j]:
                count += 1
        tmp.insert(i-count, x[i])
                
print(tmp)
        
        