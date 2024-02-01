##importar arquivos desenvolvedor
import util
import api_leitura_arquivo_log

def teste_total_erros(nome_arquivo_log, retorno_esperado):
    # Converter a string em JSON em um dicionário
    data_JSON = api_leitura_arquivo_log.retorna_json_erros_log(nome_arquivo_log)
    data_dict, erro_json = util.tratamento_json(data_JSON)

    ##verifica mensagem de erro esperada no teste
    if erro_json:
        return 'Erro obtido: ' + data_dict['Exception'] + ' Erro esperado: ' + str(retorno_esperado) + '\nResultado teste exception: ' + str(data_dict['Exception'] == retorno_esperado)
    
    ##inicia variaveis de teste
    total_de_erros = 0

    for data in data_dict:
        for chave in data.keys():
            total_de_erros += data[chave]['quantidade_de_erros']
    
    return 'Qtd de erros obtido: ' + str(total_de_erros) + ' Qtd de erros esperado: ' + str(retorno_esperado) + '\nResultado teste: ' + str(total_de_erros == retorno_esperado)

def teste_quantidade_erros_funcao(nome_arquivo_log, funcao_esperada, retorno_esperado):
    # Converter a string em JSON em um dicionário
    data_JSON = api_leitura_arquivo_log.retorna_json_erros_log(nome_arquivo_log)
    data_dict, erro_json = util.tratamento_json(data_JSON)

    ##verifica mensagem de erro esperada no teste
    if erro_json:
        return 'Erro obtido: ' + data_dict['Exception'] + ' Erro esperado: ' + str(retorno_esperado) + '\nResultado teste exception: ' + str(data_dict['Exception'] == retorno_esperado)

    ##inicia variaveis de teste
    total_de_erros = 0

    for data in data_dict:
        for chave in data.keys():
            if funcao_esperada in chave:
                total_de_erros += data[chave]['quantidade_de_erros']
    
    return 'Qtd de erros obtido: ' + str(total_de_erros) + ' Qtd de erros esperado: ' + str(retorno_esperado) + '\nResultado teste: ' + str(total_de_erros == retorno_esperado)

def teste_tipo_qtd_erros_funcao(nome_arquivo_log, funcao_esperada, erro_esperado, retorno_esperado):
    # Converter a string em JSON em um dicionário
    data_JSON = api_leitura_arquivo_log.retorna_json_erros_log(nome_arquivo_log)
    data_dict, erro_json = util.tratamento_json(data_JSON)

    ##verifica mensagem de erro esperada no teste
    if erro_json:
        return 'Erro obtido: ' + data_dict['Exception'] + ' Erro esperado: ' + str(retorno_esperado) + '\nResultado teste exception: ' + str(data_dict['Exception'] == retorno_esperado)

    ##inicia variaveis de teste
    total_de_erros = 0

    for data in data_dict:
        for chave in data.keys():
            if funcao_esperada in chave:
                total_de_erros += data[chave]['quantidade_de_erros']
                for erro in data[chave]['erros']:
                    if erro_esperado in erro.keys():
                        total_de_erros = erro[erro_esperado]

    return 'Qtd de erros obtido: ' + str(total_de_erros) + ' Qtd de erros esperado: ' + str(retorno_esperado) + '\nResultado teste: ' + str(total_de_erros == retorno_esperado)

if __name__ == '__main__':

    print('=====================================================')
    print('Testes total de erro:\n')
    print(teste_total_erros('log.txt', 179))
    print(teste_total_erros('log.txt', 200))
    print(teste_total_erros('log.txt', 0))
    print(teste_total_erros('log.txt', 'Leonardo'))
    print(teste_total_erros('log.txt', -1))
    print(teste_total_erros('lo.txt', 'teste'))
    print(teste_total_erros('ltxt', 'Arquivo de log nao encontrado'))

    print('=====================================================')
    print('Testes erros por funcao\n')
    print(teste_quantidade_erros_funcao('log.txt', 'GEDI_USB_StatusGet', 6))
    print(teste_quantidade_erros_funcao('log.txt', 'GEDI_USB_StatusGet', 2))
    print(teste_quantidade_erros_funcao('log.txt', 'GEDI_USB_StatusGet', 'Leonardo@!#'))
    print(teste_quantidade_erros_funcao('log.txt', 'GEDI_BT_Disconnect', 2))
    print(teste_quantidade_erros_funcao('log.txt', 'GEDI_BT_Disconnect', 6))
    print(teste_quantidade_erros_funcao('log.txt', 'GEDI_SMART_Status', 7))
    print(teste_quantidade_erros_funcao('log.txt', 'GEDI_SMART_Status', 4))
    print(teste_quantidade_erros_funcao('l.txt', 'GEDI_BT_Disconnect', 6))
    print(teste_quantidade_erros_funcao('lo', 'GEDI_SMART_Status', 'Arquivo de log nao encontrado'))
    print(teste_quantidade_erros_funcao('lo', 'GEDI_SMART_Status', 'Arquivo'))

    print('=====================================================')
    print('Testes se encontrou o erro e a quantidade por funcao\n')
    print(teste_tipo_qtd_erros_funcao('log.txt', 'GEDI_BT_Disconnect', 'GEDI_RET_TEST_FAIL', 1))
    print(teste_tipo_qtd_erros_funcao('log.txt', 'GEDI_BT_Disconnect', 'GEDI_RET_TEST_FAIL', 4))
    print(teste_tipo_qtd_erros_funcao('log.txt', 'GEDI_BT_Disconnect', 'GEDI_RET_OK', -1))
    print(teste_tipo_qtd_erros_funcao('log.txt', 'GEDI_BT_Disconnect', 'GEDI_RET_OK', 2))
    print(teste_tipo_qtd_erros_funcao('log.txt', 'GEDI_BT_Disconnect', 'GEDI_RET_OK', 'Leo'))
    print(teste_tipo_qtd_erros_funcao('log.txt', 'GEDI_BT_Disconnect', 'leonardo', '3'))
    print(teste_tipo_qtd_erros_funcao('log.txt', 'GEDI_SMART_Status', 'GEDI_RET_FUNCTION_NOT_FOUND', 3))
    print(teste_tipo_qtd_erros_funcao('log.txt', 'GEDI_SMART_Status', 'GEDI_RET_FUNCTION_NOT_FOUND', 7))
    print(teste_tipo_qtd_erros_funcao('log.txt', 'GEDI_SMART_Status', 'GEDI_RET_OUT_OF_BOUNDS', 1))
    print(teste_tipo_qtd_erros_funcao('l.txt', 'GEDI_SMART_Status', 'GEDI_RET_FUNCTION_NOT_FOUND', 'teste'))
    print(teste_tipo_qtd_erros_funcao('txt', 'GEDI_SMART_Status', 'GEDI_RET_OUT_OF_BOUNDS', 'Arquivo de log nao encontrado'))