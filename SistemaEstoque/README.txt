
 SISTEMA DE CONTROLE DE ESTOQUE
 Autor: Mitchelle Mendes da Silva
 Desenvolvimento individual


1. DESCRIÇÃO
Sistema web para controle de estoque com cadastro, consulta,
edição, exclusão, filtro por nome, relatório e autenticação.

2. TECNOLOGIAS
Java, JSP, JSTL, Servlet, JDBC, MySQL, HTML, CSS, Bootstrap 5.3.3,
Jetty 11.0.15, Maven, MVC, DAO

3. COMO RODAR NO LUBUNTU

Passo 1 - Banco de dados:
- Abra o MySQL
- Rode o arquivo script.sql que está na pasta do ZIP
- Ele cria o banco estoque_db e as tabelas produtos e usuarios

Passo 2 - Rodar o sistema:
- Abra o terminal na pasta do projeto
- Rode: mvn org.eclipse.jetty:jetty-maven-plugin:11.0.15:run

Passo 3 - Acessar:
- Abra o navegador em: http://localhost:8080
- Login: admin
- Senha: 1234