# Python com SQLite e TKinter

## Olá, me chamo Pedro, estudo Análise e Desenvolvimento de sistemas.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=0E76A8)](https://www.linkedin.com/in/pedro-henrique-matias-de-almeida-silva-9a59b2252/)
[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram)](https://www.instagram.com/pelyhenrique/)

### Nesse projeto faço uma conexão entre o banco de dados SQLite com python para adicionar registros no banco de dados e com a opção de exportar a planilha em formato de Excel.

Começamos importando as bibliotecas, Tkinter: para gerar criar a janela do sistema de cadastro, Sqlite: para realizar a conexão com o banco e criar as tabelas (obs.:Aqui podemos usar outros bancos de dados, usei o sqlite por ser mais leve e ser utilizado em um projeto local), pandas: para poder tratar os dados e gerar o arquivo Excel, e o tkinter messagebox para poder apresentar mensagens de erro se acontecer.

### Criando o banco de dados

Na primeira parte do código criamos o banco de dados e a conexão com o código em python, um cursor para poder manipular os dados e a tabela onde serão registrados os dados.
Para o código em questão, usei os dados nome, sobrenome, telefone e email. Logo em seguida o código para criar a tabela dentro de um try, pois da próxima vez que executar o código será checado se já existe a tabela criada. Se a tabela já existir será apresentada uma mensagem de erro (aqui também poderia ser utilizado a opção de pass, para pular a fase de criação da tabela sem apresentar erro sempre que o programa for executado).
Logo em seguida será dado o commit para aprovar as mudanças no banco e depois fechar a conexão.
A criação da tabela se encontra dentro de uma função para ser chamada sempre que o botão for utilizado.

### Exportando a tabela para uma planilha.

Quando o botão de exportar é acionado, é gerada uma conexão com o banco para poder importar os dados e exportar no formato de planilha com todos os registros que já foram incluídos até o momento.

## Criação da janela, botões e labels

Nessa fase iremos criar a janela onde será rodado o código, com seus locais de preenchimento e os botões que chamam as funções inclusas no código.
Podemos escolher o tamanho da janela e o título, além de algumas outras funções do tkinter que podem ser exploradas.
Nesse código eu defini o tamanho da janela como 400x400 e travei a opção de poder aumentar o tamanho, mas isso pode ser alterado facilmente dentro do código do programa.
Os botões devem estar dentro da classe Button no tkinter que deve chamar a função referente.
No preenchimento dos labels vamos utilizar a conexão com o banco de dados para poder inserir os registros.

## Encerramento

Todo o código deve estar dentro de um loop do tkinter que só será encerrado quando for fechado o programa
