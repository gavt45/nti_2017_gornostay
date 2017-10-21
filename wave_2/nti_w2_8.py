n,k = 9, 3
d=[1,3,4,5,7,8,9,10,13]

otr_length = int((d[-1])/k)
#print("otr_length:",otr_length)

while otr_length > 0:
    jump_dots=[]
    jump_count=0
    #print("in while: ",jump_dots,jump_count)
    for dot in range(1,d[-1],otr_length):
        #print("dot:{}; dots:{}".format(dot, jump_dots))
        if not dot in d:
            break
        else:
            otr_length -= 1
            jump_count+=1
print(jump_count)
            
