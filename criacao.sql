DROP TABLE IF EXISTS cliente CASCADE;
CREATE TABLE IF NOT EXISTS cliente
(
    nome "varchar",
	email "varchar",
    senha "varchar",
    papel "varchar",
	endereco "varchar",
	dadosPag "varchar",
	saldo float,
	telefone "varchar",
    PRIMARY KEY ("email")
);

DROP TABLE IF EXISTS veterinario CASCADE;
CREATE TABLE IF NOT EXISTS veterinario
(
    nome "varchar",
	email "varchar",
	senha "varchar",
	papel "varchar",
    crmv integer,
    PRIMARY KEY ("email")
);

DROP TABLE IF EXISTS adm CASCADE;
CREATE TABLE IF NOT EXISTS adm
(
    nome "varchar",
	email "varchar",
    senha "varchar",
	papel "varchar",
    PRIMARY KEY ("email")
);

DROP TABLE IF EXISTS petshop CASCADE;
CREATE TABLE IF NOT EXISTS petshop
(
    qtdAnimais integer,
	endereco "varchar",
    PRIMARY KEY ("endereco")
);

DROP TABLE IF EXISTS historico CASCADE;
CREATE TABLE IF NOT EXISTS historico
(
	email "varchar",
	qtdPed integer,
    PRIMARY KEY ("email"),
	constraint fk_cliente
		foreign key(email)
			references cliente(email)
);
DROP TABLE IF EXISTS pedido CASCADE;
CREATE TABLE IF NOT EXISTS pedido
(
	email "varchar",
	numPed integer,
	dataEnv "varchar",
	estado "varchar",
	codRastreio "varchar",
    PRIMARY KEY ("email"),
	constraint fk_cliente
		foreign key(email)
			references cliente(email)
);

DROP TABLE IF EXISTS estoque CASCADE;
CREATE TABLE IF NOT EXISTS estoque
(
	produto "varchar",
	quantidade integer
);

DROP TABLE IF EXISTS adocao CASCADE;
CREATE TABLE IF NOT EXISTS adocao
(
	nome "varchar",
	espécie "varchar"
);



select * from cliente
select * from veterinario
select * from adm
select * from historico
select * from pedido