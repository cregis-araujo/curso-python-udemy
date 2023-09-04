#Crie uma função que multiplica todos os argumentos
#não nomeados recebidos
#Retorne o total para uma variável e mostre o valor
#da variável.

#Crie uma função que fala o se o valor se um número é par ou ímpar.
#Retorne se o número é par ou ímpar.

def mult(*args):
    total=1
    for numero in args:
        total=total*numero
    return total

resultado=mult(1,2,3,4,5,6)
print(resultado)


def impar_ou_par(numero):
    numero=input('Digite um número: ')
    if (int(numero) % 2) == 0:
        return print('Esse número é par')
    return print('Esse número é ímpar')
numero=''
impar_ou_par(numero)
