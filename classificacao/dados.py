import csv

def carregar_acessos():
    dados = []
    marcacoes = []

    arquivo = open('acesso.csv', 'rb')
    leitor = csv.reader(arquivo)
    next(leitor)
    for acessou_home, acessou_como_funciona, acessou_contato, comprou in leitor:
        dados.append([int(acessou_home), int(acessou_como_funciona), int(acessou_contato)])
        marcacoes.append(int(comprou))

    return dados, marcacoes
def carregar_buscas():

    X = []
    Y = []

    arquivo = open('busca.csv', 'rb')
    leitor = csv.reader(arquivo)

    leitor.next()

    for home,busca,logado,comprou in leitor:

        dado = ([int(home), busca, int(logado)])
        X.append(dado)
        Y.append(int(comprou))

    return X, Y