drop database if exists Api;

create database Api;

use Api;

CREATE TABLE Usuario (

user_id int primary key  auto_increment,
user_nome text (100) not null,
user_data_nasc date not null,
user_endereco text (100) not null,
user_cpf varchar (11) not null unique,
user_email varchar (100) not null unique,
user_senha varchar (26) not null,
user_parentesco varchar (20) not null,
user_profissao text (50) not null,
user_como_chegou varchar (50) not null
);


CREATE TABLE Comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto_comentario LONGTEXT NOT NULL,
    user_id INT NOT NULL, #CHAVE ESTRANGEIRA DO USUARIO QUE POSTOU O COMENTARIO.
    post_id INT NOT NULL, #CHAVE ESTRANGEIRA DO POST Q FOI FEITO, PARA DIRECIONAR PARA QUAL FOI, PRECISA SER FEITO UM POST.SQL MAIS TARDE.
    comentario_para INT NULL, #ESTOU EM DÚVIDA NESSE, POIS ELE ACABA SENDO UMA INFORMÇÃO DUPLICADA, BASICAMENTE FAZ O QUE O POSTAGEM_ID FAZ, ENT N SEI SE É NECESSARIO.
    data_postada date NOT NULL
);


CREATE TABLE Post (

    post_id int auto_increment primary key,
    post_caracters varchar (500) not null

)

