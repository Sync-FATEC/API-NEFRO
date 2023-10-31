drop database if exists Api;

create database Api;

use Api;

CREATE TABLE usuario (

user_id int primary key  auto_increment,
user_nome varchar (100) not null,
user_data_nasc date not null,
user_endereco varchar (100) not null,
user_cpf varchar (11) not null unique,
user_email varchar (100) not null unique,
user_senha varchar (26) not null,
user_parentesco varchar (20) not null,
user_profissao varchar (50) not null,
user_como_chegou varchar (50) not null,
user_admin BOOLEAN default false
);


CREATE TABLE comentarios (
com_id INT AUTO_INCREMENT PRIMARY KEY,
com_historia LONGTEXT NOT NULL,
com_data DATE,
com_imagem varchar (255),
com_nome_filho varchar (255),
com_aprovado BOOLEAN default false,
com_denuncia BOOLEAN default false,
fk_user_id INT,
fk_com_id INT,
FOREIGN KEY (fk_user_id) REFERENCES usuario(user_id),
FOREIGN KEY (fk_com_id) REFERENCES comentarios(com_id)
);
