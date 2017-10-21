import operator
from random import randint
n = int(input())
n_list = list(map(int, input().split()))
n_list_xored = n_list[0]
if n > 1:
    for i in range(1,len(n_list)):
        n_list_xored = operator.xor(n_list_xored,n_list[i])
rnd1 =randint(0,2**30)
while rnd1 in n_list:
    rnd1 = randint(0,2**30)
rnd2 = operator.xor(n_list_xored,rnd1)
print(rnd1,rnd2)
