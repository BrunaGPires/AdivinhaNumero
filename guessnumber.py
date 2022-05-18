import random

def num(x):
    ran_num = random.randint(1,x)
    num = 0
    while num != ran_num:
        num = int(input(f'Adivinhe o numero entre 1 e {x}:'))
        if num < ran_num:
            print('Tente de novo. Valor muito baixo')
        elif num > ran_num:
            print('Tente de novo. Valor muito grande')

    print(f'Parabens você conseguiu! Você adivinhou o número {ran_num} certo!')

num(100)
