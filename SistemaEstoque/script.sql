CREATE DATABASE estoque_db;
USE estoque_db;

CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario VARCHAR(100) NOT NULL,
  senha VARCHAR(100) NOT NULL,
  nome VARCHAR(100)
);

CREATE TABLE produtos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  descricao VARCHAR(255),
  quantidade INT NOT NULL,
  preco DECIMAL(10,2) NOT NULL,
  categoria VARCHAR(50) NOT NULL,
  data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO usuarios (usuario, senha, nome) VALUES ('admin', '1234', 'Mitchelle');

INSERT INTO produtos (nome, descricao, quantidade, preco, categoria) VALUES
('Batom Matte', 'Vermelho Ruby Woo', 25, 29.90, 'Batom'),
('Base Líquida', 'Cor Bege Médio - Cobertura alta', 15, 59.90, 'Base'),
('Paleta de Sombras', '12 cores nude e rosé', 10, 89.90, 'Sombra'),
('Rímel Volume', 'Preto - À prova dágua', 30, 34.90, 'Rímel'),
('Blush Rosé', 'Tom pêssego', 20, 24.90, 'Blush');