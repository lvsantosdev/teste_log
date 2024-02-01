<h1 align="left"> Desafio de Engenharia de Qualidade de Software </h1>

<p align="left">
<img loading="lazy" src="https://img.shields.io/badge/status-finalizado-blue"/>
</p>

<h2 align="left"> Descrição do projeto </h2>

<p align="left">
Este projeto possui dois objetivos, sendo o primeiro deles realizar a leitura de um arquivo txt de log que contém mensagens de erros de funções de um equipamento, agrupando estas mensagens por cada função e imprimindo essa informação em um relatório para o usuário. Como objetivo secundário, para garantir a confiabilidade do código, foi desenvolvido um script que contém funções de testes, que verificam se o retorno da API está condizente com as informações passadas para o usuário.
</p>

# :hammer: Funcionalidades do projeto

- `Relatório`: O arquivo main.py se comunica com uma API que retorna um json agrupando os erros por função e imprime essa informação para o usuário
- `Teste total de erros`: O arquivo testes.py contém a função teste_total_erros, que recebe como input o nome do arquivo a ser lido e a quantidade de erros esperada, retornando uma mensagem indicando o sucesso ou falha do teste. Caso seja passado um nome de arquivo que não existe, é possível verificar se a mensagem de erro está condizente com a documentação.
- `Funcionalidade 2a`: O arquivo testes.py contém a função teste_quantidade_erros_funcao, que recebe como input o nome do arquivo a ser lido, a quantidade de erros esperada e o nome da função que deseja verificar, retornando uma mensagem indicando o sucesso ou falha do teste. Caso seja passado um nome de arquivo que não existe, é possível verificar se a mensagem de erro está condizente com a documentação.
- `Funcionalidade 3`: O arquivo testes.py contém a função teste_tipo_qtd_erros_funcao, que recebe como input o nome do arquivo a ser lido, a quantidade de erros esperada, o nome da função e qual o tipo de erro esperada, retornando uma mensagem indicando o sucesso ou falha do teste. Caso seja passado um nome de arquivo que não existe, é possível verificar se a mensagem de erro está condizente com a documentação.

# 📁 Acesso ao projeto

**Esse projeto é de aceso livre podendo ser baixado nesse repositório e modificado de acordo com o que desejar**

# 🛠️ Abrir e rodar o projeto

**Para rodar o projeto, basta seguir a instalação padrão do python de acordo com seus sistema operacional, na versão 3.11.1**
