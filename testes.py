##importar bibliotecas python
import json
##importar arquivos desenvolvedor
import api_leitura_arquivo_log

def teste_total_erros(quantidade_esperada_erros):
    # Converter a string em JSON em um dicionário
    data_JSON = api_leitura_arquivo_log.retorna_json_erros_log()
    data_dict = json.loads(data_JSON)

    ##inicia variaveis de teste
    total_de_erros = 0

    for data in data_dict:
        for chave in data.keys():
            total_de_erros += data[chave]['quantidade_de_erros']
    
    return total_de_erros == quantidade_esperada_erros

def teste_quantidade_erros_funcao(funcao_esperada, quantidade_esperada_erros):
    # Converter a string em JSON em um dicionário
    data_JSON = api_leitura_arquivo_log.retorna_json_erros_log()
    data_dict = json.loads(data_JSON)

    ##inicia variaveis de teste
    total_de_erros = 0

    for data in data_dict:
        for chave in data.keys():
            if funcao_esperada in chave:
                total_de_erros += data[chave]['quantidade_de_erros']
    
    return total_de_erros == quantidade_esperada_erros

def teste_tipo_erros_funcao(funcao_esperada, erro_esperado, quantidade_esperada_erros):
    # Converter a string em JSON em um dicionário
    data_JSON = api_leitura_arquivo_log.retorna_json_erros_log()
    data_dict = json.loads(data_JSON)

    ##inicia variaveis de teste
    total_de_erros = 0

    for data in data_dict:
        for chave in data.keys():
            if funcao_esperada in chave:
                total_de_erros += data[chave]['quantidade_de_erros']
                for erro in data[chave]['erros']:
                    if erro_esperado in erro.keys():
                        total_de_erros = erro[erro_esperado]

    return total_de_erros == quantidade_esperada_erros

if __name__ == '__main__':

    print('=====================================================')
    print('testes total de erro:')
    print(teste_total_erros(179))
    print(teste_total_erros(200))
    print(teste_total_erros(0))
    print(teste_total_erros('Leonardo'))
    print(teste_total_erros(-1))

    print('=====================================================')
    print('testes erros por funcao')
    print(teste_quantidade_erros_funcao('GEDI_USB_StatusGet', 6))
    print(teste_quantidade_erros_funcao('GEDI_USB_StatusGet', 2))
    print(teste_quantidade_erros_funcao('GEDI_USB_StatusGet', 'Leonardo@!#'))
    print(teste_quantidade_erros_funcao('GEDI_BT_Disconnect', 2))
    print(teste_quantidade_erros_funcao('GEDI_BT_Disconnect', 6))

    print('=====================================================')
    print('testes se encontrou o erro e a quantidade por funcao')
    print(teste_tipo_erros_funcao('GEDI_BT_Disconnect', 'GEDI_RET_TEST_FAIL', 1))
    print(teste_tipo_erros_funcao('GEDI_BT_Disconnect', 'GEDI_RET_TEST_FAIL', 4))
    print(teste_tipo_erros_funcao('GEDI_BT_Disconnect', 'GEDI_RET_OK', -1))
    print(teste_tipo_erros_funcao('GEDI_BT_Disconnect', 'GEDI_RET_OK', 2))
    print(teste_tipo_erros_funcao('GEDI_BT_Disconnect', 'GEDI_RET_OK', 'Leo'))
    print(teste_tipo_erros_funcao('GEDI_BT_Disconnect', 'leonardo', '3'))