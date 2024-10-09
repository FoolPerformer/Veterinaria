import psycopg2

hostname = 'localhost'
database = 'vet'
username = 'postgres'
pwd = '123456'
port_id = 5432
conn = None
cur = None
email_geral = None

# to do: menu cliente, menu adm, menu veterinario
#Func to do: verificar consultas(veterinario), verificar estoque(cliente), verificar adocao(cliente), adicionar estoque(adm), adicionar adocao(adm), solicitar consulta(cliente), remover adocao(adm),remover estoque(adm)

conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd,
                            port=port_id)  # funcao que estabelece conexao com o bd
cur = conn.cursor()  # funcao para auxiliar nas operacoes sql

def inserir_cliente(nome, email, senha, endereco, dadospag, saldo, telefone):
    insert_scrip = f"INSERT INTO cliente values ('{nome}','{email}', '{senha}', 'cliente', '{endereco}', '{dadospag}',' {saldo}', '{telefone}');"
    cur.execute(insert_scrip)
    conn.commit()

def inserir_produto(produto, qtd):
    insert_scrip = f"INSERT INTO produto values ('{produto}',{qtd});"
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