import vet
import os

escolha = 0
while(escolha == 0):
    decisao = input("Deseja realizar o login ou se cadastrar?")
    if decisao == "cadastrar":
        vet.cadastrar()
    elif decisao == "logar":
        escolha = vet.novo_login()

if escolha == 1:
    
    while(True):
        os.system("cls")
        print()
        print("\n\n\t>>>>>>>>>>>>>>>>>>>>>>> OPCOES DE MENU <<<<<<<<<<<<<<<<<<<<<<<<");
        print("\n\n\t1. Produtos disponiveis")
        print("  \n\t2. Animais para adocao")
        print("  \n\t3. Marcar consulta")
        print("  \n\t4. SAIR")
        opcao = int(input('Informe a sua opcao: '))

        if opcao == 1:
            
            dados = vet.verificar_estoque()
            vet.imprime_estoque(dados)
            os.system("pause")

        elif opcao == 2:

            dados = vet.verifica_adocao()
            vet.imprime_adocao(dados)
            os.system("pause")
        
        elif opcao == 3:

            vet.marcar_consulta()
            os.system("pause")
        elif opcao == 4:
            break

elif escolha == 2:
    while(True):
        os.system("cls")
        print()
        print("\n\n\t>>>>>>>>>>>>>>>>>>>>>>> OPCOES DE MENU <<<<<<<<<<<<<<<<<<<<<<<<");
        print("\n\n\t1. Adicionar produto")
        print("  \n\t2. Remover um produto")
        print("  \n\t3. Adicionar Adocao")
        print("  \n\t4. Remover Adocao")
        print("  \n\t5. SAIR")
        opcao = int(input('Informe a sua opcao: '))

        if opcao == 1:
            
            vet.inserir_estoque_adm()
            os.system("pause")

        elif opcao == 2:

            vet.remover_estoque()
            os.system("pause")
        
        elif opcao == 3:

            vet.adicionar_adocao()
            os.system("pause")
        
        elif opcao == 4:

            vet.remover_adocao()
            os.system("pause")
        
        elif opcao == 5:
            break
elif escolha == 3:
    while(True):
        os.system("cls")
        print()
        print("\n\n\t>>>>>>>>>>>>>>>>>>>>>>> OPCOES DE MENU <<<<<<<<<<<<<<<<<<<<<<<<");
        print("\n\n\t1. Verificar Consultas")
        print("  \n\t2. Remover uma consulta")
        print("  \n\t3. SAIR")

        opcao = int(input('Informe a sua opcao: '))

        if opcao == 1:
            
            dados = vet.verificar_consulta()
            vet.imprime_consulta(dados)
            os.system("pause")

        elif opcao == 2:

            vet.remover_consulta()
            os.system("pause")
        
        elif opcao == 3:
            break