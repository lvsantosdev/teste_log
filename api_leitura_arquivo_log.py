##importar bibliotecas python
import json
from pathlib import Path
##importar arquivos desenvolvedor
import util
import init

def retorna_json_erros_log():
     
    ##abertura do arquivo
    diretorio = Path(__file__).parent
    diretorio_arquivo = str(diretorio) + '\log.txt'
    arquivo_log = open(diretorio_arquivo, 'r', encoding = 'utf-8')

    ##recupera parametros
    parametros = init.retorna_parametros()

    ##separa as mensagens de erro no arquivo log no formato: função;mensagem_erro
    erros = []

    for linha in arquivo_log:
            if parametros['parm1'] in linha:

                pos_ini = linha.index(parametros['parm2']) + len(parametros['parm2'])
                pos_final = linha.index(parametros['parm3'])
                funcao = linha[pos_ini:pos_final]

                pos_ini = linha.index(parametros['parm3']) + len(parametros['parm3'])
                pos_final = len(linha)
                mensagem_erro = linha[pos_ini:pos_final].strip()

                erro_funcao = funcao + ';' + mensagem_erro

                erros.append(erro_funcao)

    ##inicia variaveis
    mensagem_erro = ''
    erro_funcao = ''
    funcao = ''
    funcao_anterior = ''
    erros_funcao_anterior = []
    erros_json = []

    ##ordena a lista para poder agrupar por função
    erros.sort()

    ##loop pelos erros
    for erro_funcao in  erros:
        pos = erro_funcao.index(';')
        funcao = erro_funcao[0:pos].strip()
        mensagem_erro = erro_funcao[pos + 1:len(erro_funcao)].strip()

        ##valida se mudou a funcao em relacao o estado anterior
        if funcao != funcao_anterior and funcao_anterior != "":
            retorno_erros = util.agrupar_erros(erros_funcao_anterior)
            erro_json = {funcao_anterior:{'quantidade_de_erros': retorno_erros[1], 'erros': retorno_erros[0]}}
            erros_json.append(erro_json)
            erros_funcao_anterior = []
        funcao_anterior = funcao
        erros_funcao_anterior.append(mensagem_erro)

    ##apos finalizar o loop, adicionar o ultimo estado
    retorno_erros = util.agrupar_erros(erros_funcao_anterior)
    erro_json = {funcao_anterior:{'quantidade_de_erros': retorno_erros[1], 'erros': retorno_erros[0]}}
    erros_json.append(erro_json)

    ##transforma a saida em json
    erros_json = json.dumps(erros_json)

    ##fechar o arquivo ao final da rotina
    arquivo_log.close()

    return erros_json

if __name__ == '__main__':
    erros_json = retorna_json_erros_log()
    print(erros_json)