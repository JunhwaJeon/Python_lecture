def sum_nums(*nums):
    print('{}개의 인자 {}'.format(len(nums),nums))
    s=0
    for i in nums:
        s+=i
    m=s/len(nums)
    print('합계: {}, 평균: {}'.format(s,m))

sum_nums(10,20,30)