# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos=0

for pergunta in perguntas:
        print(pergunta['Pergunta'])
        print()
        print('Opções:')

        for opcao, valor in enumerate(pergunta['Opções']):
            print(f'{opcao}){valor}')
        print()
        
        
        try:
            resposta=int(input('Escolha uma opção: '))

            if (pergunta['Opções'][resposta]) == pergunta['Resposta']:
                print('Você acertou.👌\n')
                qtd_acertos+=1
            else:
                print('Você Errou.❌\n')
        except(IndexError):
            print('Você digitou uma opção inexistente. Resposta anulada.')
        except(ValueError):
            print('O sistema só aceita números. Resposta anulada.') 
              
        
print(f'Você acertou {qtd_acertos} de 3 questões.')
