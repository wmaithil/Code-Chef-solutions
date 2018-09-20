# cook your code here
t=int(raw_input())
for i in range(t):
    n=list(map(int ,raw_input().split()))
    dic={}
    for nb in range(1,n[0]+1):
        dic[nb]='v'
    dic[n[1]]='gold'
    #print dic
    for j in range(1,n[2]+1):
        box=list(map(int,raw_input().split()))
        dic[box[0]],dic[box[1]]=dic[box[1]],dic[box[0]]
        #print("the dic after {0} swap is {1} ".format(j,dic))
    for k,v in dic.items():
        if (v=='gold'):
            print k
            break
        