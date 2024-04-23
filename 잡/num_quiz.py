num=5

while True:
    n=int(input('1에서 10사이의 수를 맞추세요>>'))
    if n>num:
        print('{}보다 작은 수로 다시 입력>>'.format(n))
    elif n<num:
        print('{}보다 큰 수로 다시 입력'.format(n))
    else:
        print('축하합니다. {}: 정답입니다'.format(n))
        break