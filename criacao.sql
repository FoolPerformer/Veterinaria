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
	quantidade integer,
	valor float
);

DROP TABLE IF EXISTS adocao CASCADE;
CREATE TABLE IF NOT EXISTS adocao
(
	nome "varchar",
	espécie "varchar"
);

DROP TABLE IF EXISTS consulta CASCADE;
CREATE TABLE IF NOT EXISTS consulta
(
	emailCliente "varchar",
	nomeTutor "varchar",
	nomePet "varchar",
	raca "varchar",
	dataConsulta "varchar",
	horario "varchar",
	motivo "varchar",
	email "varchar",
    PRIMARY KEY ("email"),
	constraint fk_veterinario
		foreign key(email)
			references veterinario(email)
);

insert into veterinario values ('jorge','jorge@gmail','asda','chefe', 12);
insert into adm values ('caio','caio@gmail','123456','dono');
insert into estoque values ('racao Pedgree', 123, 15);
insert into estoque values ('mordedor', 20, 10);
insert into estoque values ('Cama', 5, 150);
insert into adocao values ('Branquinho', 'coelho');
insert into adocao values ('Bicarbonato', 'gato');


select * from cliente
select * from veterinario
select * from adm
select * from historico
select * from pedido
select * from estoque
select * from consulta
select * from adocao