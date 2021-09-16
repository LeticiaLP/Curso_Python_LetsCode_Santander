import requests
from datetime import date, datetime
# 1 REQUISIÇÃO E SELEÇÃO DOS DADOS SOBRE VACINAÇÃO
class DadosVacina:
    # REALIZANDO E AUTORIZANDO A REQUISIÇÃO PARA O ACESSO À API
    def autorizarRequisicao(self):

        url_ = "https://imunizacao-es.saude.gov.br/_search?scroll=1m"
        url = "https://imunizacao-es.saude.gov.br/_search/scroll"
        user = "imunizacao_public"
        key = "qlto5t&7r_@+#Tlstigi"

        body_ = {
            "size": 10000
        }
        req_ = requests.post(url_, json=body_, auth=(user, key))

        body = {
            "scroll_id": req_.json()["_scroll_id"],
            "scroll": "1m"
        }
        req = requests.post(url, json=body, auth=(user, key))

        if (req.status_code != 200):
            print('Error:', req.text)

        dadosBrutos = []
        cont = 0
        while cont < 50:
            req = requests.post(url, json=body, auth=(user, key))
            dadosBrutos.append(req.json()["hits"]["hits"])
            cont = cont + 1

        return dadosBrutos

    # ORGANIZANDO OS DADOS DA API
    def dadosVacinacao(self):
        dadosIndices = []
        dadosValidos = []

        vacinacao = self.autorizarRequisicao()
        # criando uma nova lista (dadosIndice) de dicionários com uma das chaves do dicionário vacinacao
        #print(len(vacinacao))
        for i in range(len(vacinacao)):
            vacinacao2 = vacinacao[i]

            for a in range(len(vacinacao2)):
                vacinacao3 = vacinacao2[a]["_source"]
                dadosIndices.append(vacinacao3)
        # criando uma lista (dadosValidos) de listas com os valores necessários para a tabela
        for dados in dadosIndices:
            dadosValidos.append([dados["paciente_idade"], dados["paciente_racaCor_valor"], dados["paciente_enumSexoBiologico"],
                         dados["paciente_endereco_uf"], dados["vacina_codigo"], dados["vacina_categoria_nome"],
                         dados["vacina_dataAplicacao"], dados["vacina_descricao_dose"]])
        # ordenando a lista por datas
        dadosOrdenados = sorted(dadosValidos, key=lambda datas: datas[6])
        # inserindo um header no início da lista com os nomes de cada posição
        dadosOrdenados.insert(0, ["Idade", "Raça", "Sexo", "Estado", "Vacina", "Categoria Vacinada", "Aplicação", "Dose"])
        # convertendo a data (String) para o tipo date
        for i in range(1, len(dadosOrdenados)):
            dadosOrdenados[i][6] = datetime.strptime(dadosOrdenados[i][6][:10], "%Y-%m-%d").date()

        return dadosOrdenados





