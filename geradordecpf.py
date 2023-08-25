import sys
import random


while True:


    
    cpf_gerado_pelo_calculo=0
    digito_2=0
    digito_1=0
    
    opcao=input('Deseja gerar um novo CPF? S[im] ou N[ão] ')
    if opcao == 'N':
        sys.exit()
    else:

        CPF_digitado_tratado=''
        for i in range(9):
            cpf_digito=random.randint(0,9)
            CPF_digitado_tratado+=str(cpf_digito)
        
        mult_regressivo=10
        somadamultiplicacao=0
        for cpf_digito in CPF_digitado_tratado[0:9]:
            cpf_digito_int=int(cpf_digito)
            
            cpf_multiplicado_por_fat10=cpf_digito_int*mult_regressivo
            somadamultiplicacao+=cpf_multiplicado_por_fat10
            mult_regressivo+=-1
        
        resultado_mult_10=somadamultiplicacao * 10
        digito_1=resultado_mult_10 % 11
        if digito_1 >9:
            digito_1=0
        else:
            digito_1=digito_1

        CPF_digitado_tratado+=str(digito_1)
        
        mult_regressivo_2=11
        somadamultiplicacao_2=0
        for cpf_digito in CPF_digitado_tratado[0:10]:
            cpf_digito_int=int(cpf_digito)
            
            cpf_multiplicado_por_fat10_2=cpf_digito_int*mult_regressivo_2
            somadamultiplicacao_2+=cpf_multiplicado_por_fat10_2
            mult_regressivo_2+=-1
        
        resultado_mult_11=somadamultiplicacao_2 * 10
        digito_2=resultado_mult_11 % 11
        if digito_2 >9:
            digito_2=0
        else:
            digito_2=digito_2

        cpf_gerado_pelo_calculo= f'{CPF_digitado_tratado[0:9]}{digito_1}{digito_2}'

        print('CPF válido gerado: ',cpf_gerado_pelo_calculo)
