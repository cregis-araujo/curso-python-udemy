import os
palavrasecreta='perfume'
letrasacertadas=''
numerotentativas=0

while True:

    letradigitada=input('Digite uma letra:' )
    numerotentativas+=1

    e_inteiro=letradigitada.isdigit()
    if (e_inteiro==True) or len(letradigitada)>1:
        print('Digite apenas uma letra.')
        continue
    else:
        if letradigitada in palavrasecreta:
            letrasacertadas+=letradigitada

        palavraformada=''
        for letra_secreta in palavrasecreta:
            if letra_secreta in letrasacertadas:
                palavraformada+=letra_secreta
            else:
                palavraformada+='*'
        print('Palavra formada:', palavraformada)

        if palavraformada == palavrasecreta:
            os.system('cls')
            print('Você Ganhou!!')
            print('A palavra secreta era',palavrasecreta)
            print('Tentativas', numerotentativas)
            letrasacertadas=''
            numerotentativas=0
            break
