org_list=[8,5,12,34,3,2,97,23,45]

def partition(blist):
    alist=blist
    pivot=alist[0]; exchange_idx=0
    while True:
        inf_idx, sup_idx=0,0
        for i in range(-1,-1*len(alist),-1):
            if pivot>alist[i]:
                inf_idx=i; break
        for i in range(len(alist)):
            if alist[i]>pivot:
                sup_idx=i; break
        if sup_idx>len(alist)+inf_idx: 
            break
        else: 
            alist[inf_idx], alist[sup_idx]=alist[sup_idx], alist[inf_idx]
            exchange_idx=sup_idx
    alist[0],alist[exchange_idx]=alist[exchange_idx],alist[0]
    return alist

a=partition(org_list)
print(a)