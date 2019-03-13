from random import randint

rand = randint(1, 100)
cnt = randint(3, 8)

def check_number(num, n):
    for i in range(0, n, 1):
        a = input('> ')
        if a.isdigit():
            a = int(a)
        else:
            print('Ввод неверный. Попробуй начать сначала.')
            return
                
        if a < num:
            if i == n - 1:
                print('Ты проиграл :(')
            else:
                print('Попробуй ввести число больше')
        elif a > num:
            if i == n - 1:
                print('Ты проиграл :(')
            else:
                print('Попробуй ввести число меньше')
        else:
            print('Ты угадал!')
            
if cnt < 5:
    atmpt = 'попытки'
else:
    atmpt = 'попыток'
    
print(f'Я загадала число от 1 до 100. Попробуй угадать его! \nУ тебя есть {cnt} {atmpt} ;)')
check_number(rand, cnt)



