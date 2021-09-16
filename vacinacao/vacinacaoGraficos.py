from vacinacaoTabelas import TabelaVacina
from PIL import Image
from IPython.display import display
import requests
# 3 CRIAÇÃO DOS GRÁFICOS
class GraficoVacina:
    # MÉTODO PARA CONSTRUIR A CHAVE DATASET (com legenda e dados) DA URL DA API QuickChart PARA GRÁFICO DE BARRA
    def pegarDadosBar(self, y, legendas):

        if type(y[0]) == list:
            dados1 = []
            # associa um dado (linha de uma lista) a uma legenda
            for a in range(len(y)):
                dados1.append({
                    "label": legendas[a],
                    "data": y[a]
                })

            return dados1

        else:
            dados2 = [
                {
                "label": legendas[0],
                "data": y
                }
            ]

            return dados2

    # MÉTODO PARA CONSTRUIR A CHAVE DATASET (com dados) DA URL DA API QuickChart PARA GRÁFICO DE PIZZA
    def pegarDadosPie(self, y):
        dados = []

        dados.append({
            "data": y,
            "backgroundColor": [('yellow'), ('turquoise')]
        })

        return dados

    # MÉTODO PARA CONSTRUIR A CHAVE DATASET (com dados e legenda) DA URL DA API QuickChart PARA GRÁFICO DE BARRA COM DETALHES
    def pegarDadosBar2(self, y, legendas):

        dados1 = []

        dados1.append({
            "label": legendas,
            "data": y,
            "backgroundColor": 'blue',
            "borderColor": 'blue',
            "borderWidth": 1
        })

        return dados1

    # MÉTODO PARA DEFINIR O TIPO DE GRÁFICO
    def criarTitulo(self, titulo = ""):

        if titulo != "":
            tela = "true"
        else:
            tela = "false"

        titulo1 = {
            "display": tela,
            "text": titulo
        }

        return titulo1

    # MÉTODO PARA CRIAR UM DICIONÁRIO REPRESENTANDO O GRÁFICO
    def criarGrafico(self, x, y, legendas, tipo="", titulo=""):
        dados = self

        opcao = self.criarTitulo(titulo)

        if tipo == "bar":

            if len(legendas) == 2:
                dados = self.pegarDadosBar(y, legendas)
            else:
                dados = self.pegarDadosBar2(y, legendas)

        elif tipo == "pie":
            dados = self.pegarDadosPie(y)

        if tipo == "bar" and len(legendas) != 2:

            grafico = {
                "type": tipo,
                "data": {
                    "labels": x,
                    "datasets": dados
                }
            }

            return grafico

        else:

            grafico = {
                "type": tipo,
                "data": {
                    "labels": x,
                    "datasets": dados
                },
                "options": {
                    "title": opcao
                }
            }

            return grafico

    # MÉTODO PARA FAZER A REQUISIÇÃO DA API QuickChart
    def chamarApiGrafico(self, grafico):
        url = "https://quickchart.io/chart"
        requisicao = requests.get(f"{url}?c={str(grafico)}")

        return requisicao.content

    # MÉTODO PARA SALVAR O GRÁFICO NUM ARQUIVO DE IMAGEM (.png / .jpg)
    def salvarGrafico(self, arquivo, conteudo):
        with open(arquivo, "wb") as imagem:
            imagem.write(conteudo)

    # MÉTODO PARA EXIBIR A IMAGEM NA IDE
    def mostrarGrafico(self, arquivo):
        imagem = Image.open(arquivo)
        display(imagem)

    # MÉTODO PARA PLOTAR UM GRÁFICO EM BARRA COM OS DADOS DE DOSES E DATAS DE VACINAÇÃO
    def graficoDoseData(self):
        t = TabelaVacina()
        dados = t.tabelaDoseData()
        dadosDose1 = []
        dadosDose2 = []
        dadosDataX = []
        legendas = ["1ª Dose", "2ª Dose"]

        for d in dados:
            dadosDose1.append(d[1])

        for e in dados:
            dadosDose2.append(e[2])

        for f in dados:
            dadosDataX.append(f[0])

        grafico = self.criarGrafico(dadosDataX, [dadosDose1, dadosDose2], legendas, "bar", "Quantidade de Doses de Vacinas Anti-Covid Aplicadas por Mês")

        graficoChamada = self.chamarApiGrafico(grafico)

        self.salvarGrafico("Dose_por_Data.png", graficoChamada)

        self.mostrarGrafico("Dose_por_Data.png")

    # MÉTODO PARA PLOTAR UM GRÁFICO PIZZA COM OS DADOS DE SEXO F/M DE PESSOAS VACINADAS
    def graficoSexo(self):
        t = TabelaVacina()
        dadosSexo = t.tabelaSexo()[1]
        dadosX = ["Feminino", "Masculino"]

        grafico = self.criarGrafico(dadosX, dadosSexo, "", "pie", "Quantidade de Pessoas Vacinadas por Sexo")

        graficoChamada = self.chamarApiGrafico(grafico)

        self.salvarGrafico("Vacinacao_Por_Sexo.png", graficoChamada)

        self.mostrarGrafico("Vacinacao_Por_Sexo.png")

    # MÉTODO PARA PLOTAR UM GRÁFICO EM BARRA COM OS DADOS DOS TIPOS DE VACINAS APLICADAS
    def graficoVacina(self):
        t = TabelaVacina()
        dadosVacina = t.tabelaVacina()[1]
        dadosX = t.tabelaVacina()[0]
        legendas = ["Vacinas Aplicadas"]

        grafico = self.criarGrafico(dadosX, dadosVacina, legendas, "bar", "")

        graficoChamada = self.chamarApiGrafico(grafico)

        self.salvarGrafico("Vacinas_Aplicadas.png", graficoChamada)

        self.mostrarGrafico("Vacinas_Aplicadas.png")







