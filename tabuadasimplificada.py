from time import sleep
print('_='*10)
print('Meu Jogo de Tabuadas')
print('_='*10)
num = int(input('Digite um número: '))
print('Processando...')
sleep(3)
for c in range(1, 11):
    print('\033[35m{} x {:2} = {}\033[m'.format(num, c, num*c))