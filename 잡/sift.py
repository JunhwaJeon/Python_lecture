def sift(n): ## n이하의 소수를 에라토스테네스의 체를 이용하여 찾는 함수
    num=[]
    for i in range(1,n+1):
        for j in range(2,i):
            if i%j==0:
                break
            elif j==i-1 and i%j!=0:
                num.append(i)
                break
    return num

print('{}이하의 소수는: {}'.format(1000, sift(1000)))