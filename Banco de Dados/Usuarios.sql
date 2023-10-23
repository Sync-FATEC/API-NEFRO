drop database if exists Api;

create database Api;

use Api;

create table Usuario (

user_id int primary key  auto_increment,
user_nome text (100) not null,
user_data_nasc date not null,
user_endereco text (100) not null,
user_cpf varchar (11) not null,
user_email varchar (100) not null,
user_senha varchar (26) not null,
user_parentesco text (20) not null,
user_profissao text (50) not null,
user_como_chegou text (50) null
);