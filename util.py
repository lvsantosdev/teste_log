##importar bibliotecas python
import json

def agrupar_erros(mensagens_erro):
    ##orderna os erros para agrupamento
    mensagens_erro.sort()

    ##inicia as variaveis
    mensagens_erro_agrupadas = []
    mensagem_erro_anterior = ''
    qtd_erros = 0
    total_erros = 0

    ##loop pelas mensagens de erro
    for mensagem_erro in mensagens_erro:

        ##valida se mudou mensagem de erro em relacao o estado anterior
        if mensagem_erro != mensagem_erro_anterior and mensagem_erro_anterior != "":
            erros = {mensagem_erro_anterior:qtd_erros}
            mensagens_erro_agrupadas.append(erros)
            qtd_erros = 0

        qtd_erros += 1
        mensagem_erro_anterior = mensagem_erro
        total_erros += 1

    ##apos finalizar o loop, adicionar o ultimo estado
    erros = {mensagem_erro_anterior:qtd_erros}
    mensagens_erro_agrupadas.append(erros)
    
    return mensagens_erro_agrupadas, total_erros

##funcao que recebe o json e informa se tem exception
def tratamento_json(dados_json):
    data_dict = json.loads(dados_json)
    if 'Exception' in data_dict:
        return data_dict, True
    return data_dict, False