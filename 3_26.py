line=0
n=int(input('n을 입력하시오:'))
while line!=n:
    if line%2==0:
        for i in range(n):
            print('{:2d}'.format(line*n+i+1),end=' ')
    else:
        for i in range(n,0,-1):
            print('{:2d}'.format(line*n+i),end=' ')
    print()
    line=line+1
    