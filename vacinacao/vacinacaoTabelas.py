from vacinacaoDados import DadosVacina
# 2 CRIAÇÃO DE TABELAS PARA A PLOTAGEM DOS GRÁFICOS
class TabelaVacina:
    # CRIANDO UMA TABELA (LISTA) COM OS DADOS DE DOSES E DATAS
    def tabelaDoseData(self):
        dose1 = 0
        dose2 = 0
        tabela = []

        t = DadosVacina()
        listaDados = t.dadosVacinacao()

        for i in range(1, len(listaDados)):
            listaDados[i][6] = listaDados[i][6].strftime("%d/%m/%Y")[3:10]

        for i in range(1, len(listaDados)):

            if (listaDados[i][6] != listaDados[i - 1][6]) and (listaDados[i][7] == "1ª Dose"):
                dose1 = 1
                tabela.append([listaDados[i][6], dose1, 0])

            elif (listaDados[i][6] != listaDados[i - 1][6]) and (listaDados[i][7] == "2ª Dose"):
                dose2 = 1
                tabela.append([listaDados[i][6], 0, dose2])

            elif (listaDados[i][6] == listaDados[i - 1][6]) and (listaDados[i][7] == "1ª Dose"):

                for a in range(len(tabela)):

                    if tabela[a][0] == listaDados[i][6]:

                        if tabela[a][1] == 0:
                            dose1 = 1
                            tabela[a][1] = dose1
                        else:
                            dose1 = dose1 + 1
                            tabela[a][1] = dose1

            elif (listaDados[i][6] == listaDados[i - 1][6]) and (listaDados[i][7] == "2ª Dose"):

                for b in range(len(tabela)):

                    if tabela[b][0] == listaDados[i][6]:

                        if tabela[b][2] == 0:
                            dose2 = 1
                            tabela[b][2] = dose2
                        else:
                            dose2 = dose2 + 1
                            tabela[b][2] = dose2

        return tabela
    # CRIANDO UMA LISTA COM AS QUANTIDADES DE MULHERES E HOMENS VACINADOS
    def tabelaSexo(self):
        feminino = 0
        masculino = 0
        tabela = []

        t = DadosVacina()
        listaDados = t.dadosVacinacao()

        tabela.append([0, 0])

        for i in range(1, len(listaDados)):

            if listaDados[i][2] == "F":
                feminino = feminino + 1
                tabela[0][0] = feminino

            else:
                masculino = masculino + 1
                tabela[0][1] = masculino

        tabela.insert(0, ["F", "M"])

        return tabela
    # CRIANDO UMA LISTA COM AS QUANTIDADES DE CADA TIPO DE VACINA
    def tabelaVacina(self):
        coronavac = 0
        covishield = 0
        astrazeneca = 0
        pfizer = 0
        tabela = []

        t = DadosVacina()
        listaDados = t.dadosVacinacao()

        tabela.append([0, 0, 0, 0])

        for i in range(1, len(listaDados)):

            if listaDados[i][4] == "86":
                coronavac = coronavac + 1
                tabela[0][0] = coronavac

            elif listaDados[i][4] == "85":
                covishield = covishield + 1
                tabela[0][1] = covishield

            elif listaDados[i][4] == "89":
                astrazeneca = astrazeneca + 1
                tabela[0][2] = astrazeneca

            elif listaDados[i][4] == "87":
                pfizer = pfizer + 1
                tabela[0][3] = pfizer

        tabela.insert(0, ["Coronavac", "Covishield", "Astrazeneca", "Pfizer"])

        return tabela







