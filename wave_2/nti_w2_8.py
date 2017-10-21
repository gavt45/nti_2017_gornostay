n,k = list(map(int,input().split()))
d=list(map(int,input().split()))

otr_length = 1
#print("otr_length:",otr_length)
while otr_length <= k:
    jump_dots=[]
    jump_count=0
    #print("in while: ",jump_dots,jump_count)
    if jump_count != 0 and jump_dots[-1] == d[-1]:
        print(jump_count-1)
        exit(0)
    for dot in range(1,d[-1],otr_length):
        #print("dot:{}; dots:{}; otr_length:{}".format(dot, jump_dots, otr_length))
        if not dot in d:
            #print("fot not in d")
            del jump_dots, jump_count
            jump_dots=[]
            jump_count=0
            break
        else:
            jump_dots.append(dot)
            jump_count += 1
    otr_length += 1
print(jump_count)
