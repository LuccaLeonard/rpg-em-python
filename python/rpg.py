print("seja bem vindo ao nosso rpg")
print("neste rpg iremos percorrer o percurso da sua ate o senac !!!")
print("=-"*20)

escolha = int(input("deseja jogar ? 1- sim 2-nao"))
print("=-"*20)

while escolha == 1:

    nome = str(input("Informe o seu nome :"))
    print("=-"*20)

    print("Hoje voce saiu de casa e decidiu:")
    print("1 - ir de onibus")
    print("2 - ir de uber")
    print("=-"*20)

    transporte = int(input("Qual opção voce escolhe:"))

    if transporte == 1:
        print("",nome,"escolheu ir de onibus!!")
        print("=-"*20)
    else:
        print("",nome," escolheu ir de uber!!") 
        print("=-"*20)

    if transporte == 1:
        print("voce tem duas opções de onibus:")
        print("o primeiro onibus ele te levara ao senac em 20min porem ele esta muitooo atrasado ")
        print("o segundo onibus ja chegou ele demorara 1hr para te levar ao senac e porem ele esta lotado")
        print("1 - onibus 1")
        print("2 - onibus 2")

    onibus = int(input("qual onibus voce ira escolher :"))

    if onibus == 1:
        print("voce decidiu esperar o outro onibus")
        print("=-"*20)
        print("",nome,"estava esperando o outro onibus, ")

    else:
        print("voce decidiu pegar o segundo onibus(boa sorte kkkkkk)")
    
    



    escolha = int(input("deseja jogar novamente? 1- sim 2-nao"))
 



print("obrigado por participar do nosso rpg")


