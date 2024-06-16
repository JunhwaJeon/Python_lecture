n_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]

def my_max(a):
    tmp=a[0]
    for i in range(len(a)-1):
        if tmp<a[i+1]:
            tmp = a[i+1]
    return  tmp

def my_min(b):
    tmp=b[0]
    for j in range(len(b)-1):
        if tmp>b[j+1]:
            tmp = b[j+1]
    return  tmp

print(my_max(n_list))
print(my_min(n_list))