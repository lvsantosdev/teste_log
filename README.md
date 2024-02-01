<h1 align="left"> Desafio de Engenharia de Qualidade de Software </h1>

<p align="left">
<img loading="lazy" src="https://img.shields.io/badge/status-finalizado-blue"/>
</p>

<h2 align="left"> Descrição do projeto </h2>

<p align="left">
  Este projeto possui como objetivo realizar a leitura de um arquivo de log que contém mensagens de erros de funções de um determinado equipamento, agrupando estas mensagens por cada função e imprimindo essa informação em um relatório para o usuário. 
</p>

<p align="left">
  Para garantir a confiabilidade do código, também foi desenvolvido um script que contém funções de testes, que verificam se os erros apresentados no relatório estão condizentes com o conteúdo do arquivo de log.
</p>

# :hammer: Funcionalidades do projeto

- `Funcionalidade 1`: Foi desenvolvido uma API que recebe como parametro o nome do arquivo de log a ser lido. Essa API retorna os erros agrupados em um json, e caso não encontre o arquivo informado, retornará um json com erro.

  ![evidencia_retorno_json](https://github.com/lvsantosdev/teste_log/assets/105672045/ae209837-de8d-4617-9ad4-dd1d6acd0380)

  ![evidencia_retorno_json_erro](https://github.com/lvsantosdev/teste_log/assets/105672045/b706cdd5-70e8-4c78-b9a5-ffa562219bfe)

- `Funcionalidade 2`: Imprimir em um relatório para o usuário os erros do arquivo de log agrupados por função, mostrando também a quantidade que ocorrem. O arquivo main.py se comunica com a API e imprime os erros agrupados por função. Caso ocorra algum erro na API, a informação será passada para o usuário

  ![evidencia_relatorio](https://github.com/lvsantosdev/teste_log/assets/105672045/5901f098-c94f-4318-8e79-8ce49ae6399f)

  ![evidencia_relatorio_erro](https://github.com/lvsantosdev/teste_log/assets/105672045/ef3d0fe3-4198-4261-a382-92a69f521e0a)

- `Funcionalidade 3`: O arquivo testes.py contém funções de testes desenvolvidas para validação do json retornado pela API, tanto no caso de sucesso nos testes, quanto nos casos de erro. Também é possível validar se a mensagem de erro está de acordo com o documentado. Em ambos os casos, quando o retorno conter True significa que o teste passou, enquanto False significa que o teste foi recusado.
  - `Funcionalidade 3a`: A função teste_total_erros(nome_arquivo_log, retorno_esperado) recebe como input o nome do arquivo a ser lido e a quantidade total de erros que deve conter nesse arquivo.
  
    ![evidencia_teste_total](https://github.com/lvsantosdev/teste_log/assets/105672045/96ca84bc-546d-4dc8-8429-3931fe894699)
  
  - `Funcionalidade 3b`: A função teste_quantidade_erros_funcao(nome_arquivo_log, funcao_esperada, retorno_esperado) recebe como input o nome do arquivo a ser lido, o nome da função e a quantidade total de erros esperada para essa função.

    ![evidencia_teste_fun_total](https://github.com/lvsantosdev/teste_log/assets/105672045/43198704-79c6-4c4b-834c-6c4297fc0d99)
    
  - `Funcionalidade 3c`: A função teste_tipo_qtd_erros_funcao(nome_arquivo_log, funcao_esperada, erro_esperado, retorno_esperado) recebe como input o nome do arquivo a ser lido, o nome da função, a mensagem de erro da função e a quantidade total de erros esperada para essa mensagem nessa respectiva função.

    ![evidencia_teste_fun_msg_total](https://github.com/lvsantosdev/teste_log/assets/105672045/e3a6d5d0-54cf-4089-a346-1c82a64db199)

<p align="left">
  Para facilitar na manutenção do código, o arquivo util.py contém funções de utilidade para o projeto, e o arquivo init.py contém parametros utilizados para realizar substring no arquivo de log no momento de separar as mensagens de erro e função.
</p>

# 📁 Informações complementares sobre o projeto

**O projeto foi desenvolvido na linguagem python, versão 3.11.1. Não foi utilizada nenhuma biblioteca além da padrão que já vem instalado com o python**
