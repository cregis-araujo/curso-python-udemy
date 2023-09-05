def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar



numero=int(input('Digite o número que deseja multiplicar: '))
multiplicador=int(input('Digite o multiplicador: '))
resultado= criar_multiplicador(multiplicador)

print(resultado(numero))
