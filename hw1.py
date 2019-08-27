import random

def cmp ():
    rand = random.randint(1, 100)
    while True:
        num = input('')
        if ((num.isdigit() == False and num[0] != '-') or num[0] == '0'):
            print('Error: Wrong key words type!')
            break
        else:
            num = int(num)
        if (num > 100 or num < 1):
            print('Error: Input number overflow!')
            break
        if (num > rand):
            print('bigger')
            continue
        elif (num < rand):
            print('smaller')
            continue
        else:
            print('matched')
            break

cmp()