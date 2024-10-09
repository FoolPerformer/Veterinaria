import vet

escolha = 0
while(escolha == 0):
    decisao = input("Deseja realizar o login ou se cadastrar?")
    if decisao == "cadastrar":
        vet.cadastrar()
    elif decisao == "logar":
        escolha = vet.novo_login()

if escolha == 1:
    # menu cliente
elif escolha == 2:
    # menu adm
elif escolha == 3:
    # menu vet