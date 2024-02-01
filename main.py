##importar arquivos desenvolvedor
import api_leitura_arquivo_log
import util


# Converter a string em JSON em um dicionário e verificar se houve exception
data_JSON = api_leitura_arquivo_log.retorna_json_erros_log('log.txt')
data_dict, erro_json = util.tratamento_json(data_JSON)

if erro_json:
    print(data_dict['Exception'])
else:
    ##relatorio para o usuario
    for data in data_dict:
        for chave in data.keys():
            print('================================================')
            print(f'Funcao {chave}')
            for chave_funcao in data[chave].keys():
                print(f'{chave_funcao} : {data[chave][chave_funcao]}')
            print('')

input("Press Enter to continue...")
