'''
create database livraria;
use livraria;

create table pessoas(
    nome varchar(50),
    idade int,
    cep varchar(20),
    cpf varchar(20)
);

create table livro(
    nome varchar(100),
    genero varchar(50),
    preco real
);

insert into pessoas values ('ricardo', 46, '45645465465', '4859556');
'''