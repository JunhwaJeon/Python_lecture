for i in range(1,20001):
    div1=[]
    div2=[]
    for j in range(1,i):
        if i%j==0:
            div1.append(j)
    for j in range(1,sum(div1)):
        if sum(div1)%j==0:
            div2.append(j)
    if (sum(div2)==i) & (sum(div1)!=i):
        print('{}의 친화수 {}'.format(i,sum(div1)))