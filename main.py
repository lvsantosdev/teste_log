##importar bibliotecas python
import json
##importar arquivos desenvolvedor
import api_leitura_arquivo_log


# Converter a string em JSON em um dicionário
data_JSON = api_leitura_arquivo_log.retorna_json_erros_log()
data_dict = json.loads(data_JSON)

##relatorio para o usuario
for data in data_dict:
    for chave in data.keys():
        print('================================================')
        print(f'Funcao {chave}')
        for chave_funcao in data[chave].keys():
            print(f'{chave_funcao} : {data[chave][chave_funcao]}')
        print('')