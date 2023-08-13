"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir,
apagar e listar  valores da sua lista
Não permita que o programa quebre com erros
de indice inexistentes na lista.

Nada para listar
Selecione uma opção 
Inserir, apagar, Listar:
"""
lista_compras=[]
item_lista=''
opcao=''

while True:
    print('Selecione uma opção:')
    print('(I)nserir (A)pagar (L)istar')
    opcao=input()

    if opcao == 'i' or opcao== 'I':
        item_lista=input('Digite um valor:')
        lista_compras.append(item_lista)
    elif opcao == 'a' or opcao =='A':
        valor_apagar=input('De qual índice deseja apagar?')
        valor_apagar_int=int(valor_apagar)
        try:
            lista_compras.pop(valor_apagar_int)
            print('Valor apagado com sucesso.')
        except:
              print('Índice inexistente. Repita a operação')
              continue
                
    elif opcao == 'L' or opcao =='l':
        print(lista_compras)
    else:
        print('Opção inválida')
        continue
