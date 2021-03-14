primeiro_intervalo = input("Por favor, insira o primeiro intervalo dos dados separados por intervalo:\(Obs: 0.2 0.6)\n->")

number_list = list(map(float, primeiro_intervalo.split()))

opcao = input("O que você possui? A frequência acumulada(0) ou relativa(1)?\n->")


if(opcao == "0"):
    print("Você escolheu: frequência acumulada")

    f_acumulada = input("Insira os dados: ")
elif(opcao == "1"):
    print("Você escolheu: frequência relativa")
else: 
    print("Opção não existente")