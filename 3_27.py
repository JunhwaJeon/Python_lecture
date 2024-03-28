arm=[]
for i in range(100,1000,1):
    a=i//100 #백의 자리수
    b=i//10-a*10
    c=i-100*a-10*b
    if i==a**3+b**3+c**3:
        arm.append(i)
print(arm)