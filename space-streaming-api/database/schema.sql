CREATE DATABASE IF NOT EXISTS space_streaming;

USE space_streaming;

CREATE TABLE empresas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT
);

CREATE TABLE lancamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    data DATETIME,
    status VARCHAR(50),
    foguete VARCHAR(100),
    missao VARCHAR(150),
    local VARCHAR(150),
    descricao TEXT,
    empresa_id INT NOT NULL,
    FOREIGN KEY (empresa_id) REFERENCES empresas(id)
);

CREATE TABLE videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    youtube_id VARCHAR(50) NOT NULL,
    url VARCHAR(255) NOT NULL,
    thumbnail VARCHAR(255),
    duracao VARCHAR(20),
    lancamento_id INT NOT NULL,
    FOREIGN KEY (lancamento_id) REFERENCES lancamentos(id)
);