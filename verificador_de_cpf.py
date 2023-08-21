'''
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7.
'''
import re
import sys



somadamultiplicacao=0
CPF_digitado=input('Digite o seu CPF:\n')

CPF_digitado_tratado= re.sub(r'[^0-9]','',CPF_digitado)

entrada_e_sequencial = CPF_digitado_tratado == CPF_digitado_tratado[0]\
 * len(CPF_digitado_tratado)

if entrada_e_sequencial:
    print('Você digitou dados sequenciais.')
    sys.exit()

mult_regressivo=10
for cpf_digito in CPF_digitado_tratado[0:9]:
    cpf_digito_int=int(cpf_digito)
    
    cpf_multiplicado_por_fat10=cpf_digito_int*mult_regressivo
    somadamultiplicacao+=cpf_multiplicado_por_fat10
    mult_regressivo+=-1
#print(somadamultiplicacao)
resultado_mult_10=somadamultiplicacao * 10
digito_1=resultado_mult_10 % 11
if digito_1 >9:
    digito_1=0
else:
    digito_1=digito_1

    """
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
somadamultiplicacao_2=0
mult_regressivo_2=11
for cpf_digito in CPF_digitado_tratado[0:10]:
    cpf_digito_int=int(cpf_digito)
    
    cpf_multiplicado_por_fat10_2=cpf_digito_int*mult_regressivo_2
    somadamultiplicacao_2+=cpf_multiplicado_por_fat10_2
    mult_regressivo_2+=-1
#print(somadamultiplicacao_2)
resultado_mult_11=somadamultiplicacao_2 * 10
digito_2=resultado_mult_11 % 11
if digito_2 >9:
    digito_2=0
else:
    digito_2=digito_2

cpf_gerado_pelo_calculo= f'{CPF_digitado_tratado[0:9]}{digito_1}{digito_2}'

if CPF_digitado_tratado == cpf_gerado_pelo_calculo:
    print(f' O CPF {CPF_digitado} é válido.')
else:
    print(f' O CPF {CPF_digitado} não é válido.')
