import psycopg2

hostname = 'localhost'
database = 'vet'
username = 'postgres'
pwd = '123456'
port_id = 5432
conn = None
cur = None
email_geral = None

conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd,
                            port=port_id)  # funcao que estabelece conexao com o bd
cur = conn.cursor()  # funcao para auxiliar nas operacoes sql

def inserir_cliente(nome, email, senha, endereco, dadospag, saldo, telefone):
    insert_scrip = f"INSERT INTO cliente values ('{nome}','{email}', '{senha}', 'cliente', '{endereco}', '{dadospag}',' {saldo}', '{telefone}');"
    cur.execute(insert_scrip)
    conn.commit()

def inserir_estoque(produto, qtd,preco):
    insert_scrip = f"INSERT INTO estoque values ('{produto}',{qtd},{preco});"
    cur.execute(insert_scrip)
    conn.commit()

def inserir_consulta(email,nome, especie):
    insert_scrip = f"INSERT INTO consulta values ('{email}','{nome}','{especie}');"
    cur.execute(insert_scrip)
    conn.commit()    

def inserir_adocao(nome, especie):
    insert_scrip = f"INSERT INTO adocao values ('{nome}','{especie}');"
    cur.execute(insert_scrip)
    conn.commit()
 

def inserir_veterinario(nome,senha, email,crmv):
    insert_scrip = f"INSERT INTO veterinario values ('{nome}','{senha}','{email}','veterinario' ,{crmv});"
    cur.execute(insert_scrip)
    conn.commit()

def inserir_adm(nome, email, senha):
    insert_scrip = f"INSERT INTO adm values ('{nome}','{email}', '{senha}','adm');"
    cur.execute(insert_scrip)
    conn.commit()

def inserir_historico(qtdPed, email):
    insert_scrip = f"INSERT INTO historico values ('{email}',{qtdPed});"
    cur.execute(insert_scrip)
    conn.commit()

def inserir_pedido(email, numPed, dataEnv, estado, codRastreio):
    insert_scrip = f"INSERT INTO pedido values ('{email}',{numPed},'{dataEnv}','{estado}','{codRastreio}');"
    cur.execute(insert_scrip)
    conn.commit()

def remover_consulta():

    dados = verificar_consulta()
    imprime_consulta(dados)

    nome = input("Informe o nome do cliente que voce quer remover: ") 
    delete_script = f"delete from consulta where nometutor = '{nome}'; "
    cur.execute(delete_script)
    conn.commit()

def verificar_consulta():

    email = input("informe seu email: ")
    select_script = f"select * from consulta where email = '{email}' order by dataconsulta; "
    cur.execute(select_script)
    dados = cur.fetchall()
    return dados

def imprime_consulta(dados):

    for i in dados:
        print(f"Email Cliente: {i[0]}  \t Nome Cliente: {i[1]} \t Nome Pet: {i[2]} \t Raca: {i[3]} \t Data Consulta: {i[4]} \t Hora Consulta: {i[5]} \t Motivo: {i[6]}")

def inserir_estoque_adm():

    produto = input("Informe o produto: ")
    quantidade = input("Informe a quantidade: ")
    preco = input("Informe o preco: ")

    inserir_estoque(produto,quantidade,preco)

def remover_estoque():

    dados = verificar_estoque()
    imprime_estoque(dados)

    produto = input("Informe o nome do produto que voce quer remover: ") 
    delete_script = f"delete from estoque where produto = '{produto}'; "
    cur.execute(delete_script)
    conn.commit()

def verificar_estoque():
    
    select_script = f"select * from estoque order by produto; "
    cur.execute(select_script)
    dados = cur.fetchall()
    return dados

def adicionar_adocao():

    nome = input("Informe o nome do pet: ")
    raca = input("Informe a raca do pet: ")

    inserir_adocao(nome,raca)

def remover_adocao():

    dados = verifica_adocao()
    imprime_adocao(dados)
    pet = input("Informe o nome do pet que voce quer remover: ") 
    delete_script = f"delete from adocao where nome = '{pet}'; "
    cur.execute(delete_script)
    conn.commit()   

def imprime_estoque(dados):
    for i in dados:
        print(f"Produto:{i[0]}\tquantidade:{i[1]}\t valor:{i[2]}")

def verifica_adocao():
    select_script = f"select * from adocao order by nome; "
    cur.execute(select_script)
    dados = cur.fetchall()
    return dados

def imprime_adocao(dados):
    for i in dados:
        print(f"Nome: {i[0]}  \t Especie: {i[1]}")

def inserir_consulta(emailCliente,nomeTutor, nomePet, raca, dataConsulta,horario,motivo,email):

    insert_scrip = f"INSERT INTO consulta values ('{emailCliente}','{nomeTutor}','{nomePet}','{raca}','{dataConsulta}','{horario}','{motivo}','{email}');"
    cur.execute(insert_scrip)
    conn.commit()

def marcar_consulta():
    email = input("Informe seu email: ")
    nomeTutor = input("Informe seu nome: ")
    nomePet = input("Informe o nome do seu pet: ")
    raca = input("Informe a raca do seu pet: ")
    dataConsulta = input("Informe a data que voce deseja: ")
    horario = input("Informe o horario da consulta: ")
    motivo = input("Informe o motivo da consulta: ")

    select_script = f"select * from veterinario order by nome; "
    cur.execute(select_script)
    dados = cur.fetchall()
    for i in dados:
        print(f"Nome: {i[0]} \t Email: {i[1]}")
    emailVet = input("Esses são os veterinarios disponiveis, escolha um deles e informe o email: ")

    inserir_consulta(email,nomeTutor,nomePet,raca,dataConsulta,horario,motivo,emailVet)


def novo_login():
    
    while (True):
     email_informado = input("Informe seu email: ")
     escolha = input("Você é cliente, adm ou veterinario (escreve sair para sair do programa): ")
     if escolha == "cliente":
        script = f"SELECT L.email FROM cliente L WHERE EXISTS (SELECT * FROM cliente Q WHERE Q.email = '{email_informado}' AND Q.email = L.email) ;"
        cur.execute(script)
        dados = cur.fetchall()
        retorno = 1
     elif escolha == "adm":
        script = f"SELECT L.email FROM adm L WHERE EXISTS (SELECT * FROM adm Q WHERE Q.email = '{email_informado}' AND Q.email = L.email) ;"
        cur.execute(script)
        dados = cur.fetchall()
        retorno = 2
     elif escolha == "veterinario":
        script = f"SELECT L.email FROM veterinario L WHERE EXISTS (SELECT * FROM veterinario Q WHERE Q.email = '{email_informado}' AND Q.email = L.email) ;"
        cur.execute(script)
        dados = cur.fetchall()
        retorno = 3
     elif escolha == "sair":
        retorno = 0
        break
     if not dados:
        print('Cadastro não encontrado')
     else: 
        print('Login efetuado com sucesso')
        break
    email_geral = email_informado
    return retorno

def cadastrar():
   nome = input("Informe seu nome: ")
   email = input("Informe seu email: ")
   senha = input("Informe sua senha: ")
   endereco = input("Informe seu endereco: ")
   dadosPAg = input("Informe seu dado de pagamento: ")
   saldo = input("Informe seu saldo: ")
   telefone = input("Informe seu telefone: ")

   inserir_cliente(nome,email,senha,endereco,dadosPAg,saldo,telefone)