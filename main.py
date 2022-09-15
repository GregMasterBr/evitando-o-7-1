from calendar import c
import pandas as pd 
import random 

def  ler_csv_copa_mundo():
    return pd.read_csv('data-grupo-copa-ranking-fifa.csv')


class Selecao:
    MELHOR_SCORE = 1837.6 #Score do Brasil

    # TODO: Definir um construtor com os atributos adequados tendo em vista o conteúdo de uma célula do CSV 
    def __init__(self,dadosCelula):
        #self.selecao, self.score = dadosCelula.split('|')
        dadosSelecao=dadosCelula.split('|')
        self.selecao = dadosSelecao[0]
        self.score = float(dadosSelecao[1])

    def motivacao_para_o_time_para_a_partida(self):
        """
        A pior seleção da copa (GAN, segundo a FIFA) tem 1393.5 de score, o qual equivale a 75 % do melhor score (BRA).
        Sendo assim, para que a aleatoriedade não seja tão determinante, podemos definir um intervalo inicial próximo de 75.
        Por exemplo, GAN poderia ter valores entre 70-75 (aproximadamente). 
        Por outro lado, BRA teria 70-100 (maior chance de vitória).
        """
        # TODO : Com base no comentário / insight acima, criar uma lógica para atribuir a motivação ao time .
        """
        Regra de 3 para criar a lógica da randomizar a probabilidade de chance de um time vencer dentro de um padrão aceitável.  
         1837.6 (BRA) ------ 100%
         1393.5 (GAN) ------  X%
        """
        self.ultimaMotivacao = random.uniform(70,(self.score * 100) / Selecao.MELHOR_SCORE)

        return self.ultimaMotivacao


def simulando_confrontos_fase_de_grupos():
    #Mapa em que a chave será a letra do grupo e o valor as seleções ( que ordenaremos pelas " melhores ").
    melhoresSelecoesPorGrupo = {}

    # Percorre a dataframe (dados do CSV) para criar nossos objetos / seleções .
    df = ler_csv_copa_mundo()
    for grupo , selecao_ in df.items():
        # print("GRUPO ", grupo)
        # print (selecao_)
        # TODO : Instanciar as 4 seleções do grupo , com seus respectivos nomes e score .
        sel1, sel2,sel3,sel4 = Selecao(selecao_[0]),Selecao(selecao_[1]),Selecao(selecao_[2]),Selecao(selecao_[3])
        
        # TODO : Simular os melhores do grupo com base na motivação de cada seleção .
        # Calculada a partir do seu ranking FIFA aliado a uma pitada de aleatoriedade .
        # Vai ordenar os times da ordem reversa. Do maior para o menor.
        melhoresSelecoesPorGrupo[grupo] = sorted(
            [Selecao(selecao_[0]),Selecao(selecao_[1]),Selecao(selecao_[2]),Selecao(selecao_[3])],
            key=Selecao.motivacao_para_o_time_para_a_partida,
            reverse=True)        
    

    # TODO : Imprimir os grupos , ordenados pelas melhores seleções de cada (apenas 2 se classificam)
    # Simulação da Tabela final dos confrontos das seleções nas fases de grupo    
    resultado_classificacao_fase_grupos(melhoresSelecoesPorGrupo)    

    #Mostra os 2 Classificados de cada grupo    
    classificados_para_oitavas(melhoresSelecoesPorGrupo)    

    simulando_confrontos_oitavas_de_final(melhoresSelecoesPorGrupo)


def classificados_para_oitavas(classificados):
    print("-"*50)
    print("Os classificados da fase de grupo para as Oitavas de ")
    for grupo, selecoes_motivadas in classificados.items():
        print(f"GRUPO {grupo}: ", end="")
        i=0
        for selecao_motivada in selecoes_motivadas:
            print(f"{i+1}º {selecao_motivada.selecao} ", end="")
            i+=1
            if i==2: break
        print()

def resultado_classificacao_fase_grupos(classificacao):
    # TODO : Imprimir os grupos , ordenados pelas melhores seleções de cada (apenas 2 se classificam)
    # Simulação da Tabela final dos confrontos das seleções nas fases de grupo
    print("-"*50)
    print("Simulação da Tabela final dos confrontos das seleções nas fases de grupo")
    for grupo, selecoes_motivadas in classificacao.items():
        print(f"GRUPO {grupo}: ", end="")
        for selecao_motivada in selecoes_motivadas:
            print(f"{selecao_motivada.selecao} - Última motivação: ({selecao_motivada.ultimaMotivacao:.2f}) ", end="")
        print()

def simulando_confrontos_oitavas_de_final(classificacao):
    #RENOVAR A MOTIVAÇÃO DOS TIMES PARA AS OITAVAS DE FINAL
 # Criando vaiáveis para as 2 melhores seleções de cada grupo :
    melhoresSelecoesPorGrupo = classificacao

    team1A = melhoresSelecoesPorGrupo["A"][0]
    team2A = melhoresSelecoesPorGrupo["A"][1]
    
    team1B = melhoresSelecoesPorGrupo["B"][0]
    team2B = melhoresSelecoesPorGrupo["B"][1]
    
    team1C = melhoresSelecoesPorGrupo["C"][0]
    team2C = melhoresSelecoesPorGrupo["C"][1]
    
    team1D = melhoresSelecoesPorGrupo["D"][0]
    team2D = melhoresSelecoesPorGrupo["D"][1]
    
    team1E = melhoresSelecoesPorGrupo["E"][0]
    team2E = melhoresSelecoesPorGrupo["E"][1]
    
    team1F = melhoresSelecoesPorGrupo["F"][0]
    team2F = melhoresSelecoesPorGrupo["F"][1]
    
    team1G = melhoresSelecoesPorGrupo["G"][0]
    team2G = melhoresSelecoesPorGrupo["G"][1]
    
    team1H = melhoresSelecoesPorGrupo["H"][0]
    team2H = melhoresSelecoesPorGrupo["H"][1]
    
    #classificados_para_oitavas([team1A,team2A,team1B,team2B,team1C,team2C,team1D,team2D,team1E,team2E,team1F,team2F,team1G,team2G,team1H,team2H])

    # TODO : Simular os confrontos das Oitavas de Final (randomizando novamente suas respectivas motivações) .
    # Além disso, também definir os classificados para as quartas de final em novas vaiáveis:    
    
    chaveamento_oitavas_finais1 = team1A if team1A.motivacao_para_o_time_para_a_partida() > team2B.motivacao_para_o_time_para_a_partida() else team2B
    chaveamento_oitavas_finais2 = team1C if team1C.motivacao_para_o_time_para_a_partida() > team2D.motivacao_para_o_time_para_a_partida() else team2D
    chaveamento_oitavas_finais3 = team1E if team1E.motivacao_para_o_time_para_a_partida() > team2F.motivacao_para_o_time_para_a_partida() else team2F
    chaveamento_oitavas_finais4 = team1G if team1G.motivacao_para_o_time_para_a_partida() > team2H.motivacao_para_o_time_para_a_partida() else team2H    
    chaveamento_oitavas_finais5 = team1B if team1B.motivacao_para_o_time_para_a_partida() > team2A.motivacao_para_o_time_para_a_partida() else team2A
    chaveamento_oitavas_finais6 = team1D if team1D.motivacao_para_o_time_para_a_partida() > team2C.motivacao_para_o_time_para_a_partida() else team2C
    chaveamento_oitavas_finais7 = team1F if team1F.motivacao_para_o_time_para_a_partida() > team2E.motivacao_para_o_time_para_a_partida() else team2E
    chaveamento_oitavas_finais8 = team1H if team1H.motivacao_para_o_time_para_a_partida() > team2G.motivacao_para_o_time_para_a_partida() else team2G
    
    print("-"*50)
    print("RESULTADO DOS CONFRONTO DAS OITAVAS DE FINAIS")
    print(f'{team1A.selecao} ({team1A.ultimaMotivacao:.2f}) x {team2B.selecao } ({ team2B.ultimaMotivacao:.2f})')
    print(f'{team1C.selecao} ({team1C.ultimaMotivacao:.2f}) x {team2D.selecao } ({ team2D.ultimaMotivacao:.2f})')
    print(f'{team1E.selecao} ({team1E.ultimaMotivacao:.2f}) x {team2F.selecao } ({ team2F.ultimaMotivacao:.2f})')
    print(f'{team1G.selecao} ({team1G.ultimaMotivacao:.2f}) x {team2H.selecao } ({ team2H.ultimaMotivacao:.2f})')
    print(f'{team1B.selecao} ({team1B.ultimaMotivacao:.2f}) x {team2A.selecao } ({ team2A.ultimaMotivacao:.2f})')
    print(f'{team1D.selecao} ({team1D.ultimaMotivacao:.2f}) x {team2C.selecao } ({ team2C.ultimaMotivacao:.2f})')
    print(f'{team1F.selecao} ({team1F.ultimaMotivacao:.2f}) x {team2E.selecao } ({ team2E.ultimaMotivacao:.2f})')
    print(f'{team1H.selecao} ({team1H.ultimaMotivacao:.2f}) x {team2G.selecao } ({ team2G.ultimaMotivacao:.2f})')    
    
    classificados_na_oitavas = {}

    classificados_na_oitavas[1] = [chaveamento_oitavas_finais1]
    classificados_na_oitavas[2] = [chaveamento_oitavas_finais2]
    classificados_na_oitavas[3] = [chaveamento_oitavas_finais3]
    classificados_na_oitavas[4] = [chaveamento_oitavas_finais4]    
    classificados_na_oitavas[5] = [chaveamento_oitavas_finais5]
    classificados_na_oitavas[6] = [chaveamento_oitavas_finais6]
    classificados_na_oitavas[7] = [chaveamento_oitavas_finais7]
    classificados_na_oitavas[8] = [chaveamento_oitavas_finais8]

    resultado_classificacao_oitavas_de_final(classificados_na_oitavas)
    simulando_confrontos_quartas_de_final(classificados_na_oitavas)

    return 0


def resultado_classificacao_oitavas_de_final(classificados):
    print("-"*50)
    print("Simulação da tabela dos das seleções classificados para as quartas de final")
    for chave, selecoes_motivadas in classificados.items():
        print(f"CHAVE {chave}: ", end="")
        for selecao_motivada in selecoes_motivadas:
            print(f"{selecao_motivada.selecao} - Última motivação: ({selecao_motivada.ultimaMotivacao:.2f}) ", end="")
        print()
    

def simulando_confrontos_quartas_de_final(classificados):
    # TODO : Simular os confrontos das Quartas de Final (randomizando novamente suas respectivas motivações).
    #RENOVAR A MOTIVAÇÃO DOS TIMES PARA AS OITAVAS DE FINAL
    # Criando vaiáveis para as 2 melhores seleções de cada grupo :
    selecao1 = classificados[1][0]
    selecao2 = classificados[2][0]
    selecao3 = classificados[3][0]
    selecao4 = classificados[4][0]
    selecao5 = classificados[5][0]
    selecao6 = classificados[6][0]   
    selecao7 = classificados[7][0]
    selecao8 = classificados[8][0]   

    chaveamento_quartas_finais_1_2 = selecao1 if selecao1.motivacao_para_o_time_para_a_partida() > selecao2.motivacao_para_o_time_para_a_partida() else selecao2
    chaveamento_quartas_finais_3_4 = selecao3 if selecao3.motivacao_para_o_time_para_a_partida() > selecao4.motivacao_para_o_time_para_a_partida() else selecao4

    chaveamento_quartas_finais_5_6 = selecao5 if selecao5.motivacao_para_o_time_para_a_partida() > selecao6.motivacao_para_o_time_para_a_partida() else selecao6
    chaveamento_quartas_finais_7_8 = selecao7 if selecao7.motivacao_para_o_time_para_a_partida() > selecao8.motivacao_para_o_time_para_a_partida() else selecao8
   
    print("-"*50)
    print("RESULTADO DOS CONFRONTO DAS QUARTAS DE FINAIS")
    print(f'{selecao1.selecao} ({selecao1.ultimaMotivacao:.2f}) x {selecao2.selecao} ({selecao2.ultimaMotivacao:.2f})')
    print(f'{selecao3.selecao} ({selecao3.ultimaMotivacao:.2f}) x {selecao4.selecao } ({selecao4.ultimaMotivacao:.2f})')
    print(f'{selecao5.selecao} ({selecao5.ultimaMotivacao:.2f}) x {selecao6.selecao } ({selecao6.ultimaMotivacao:.2f})')
    print(f'{selecao7.selecao} ({selecao7.ultimaMotivacao:.2f}) x {selecao8.selecao } ({selecao8.ultimaMotivacao:.2f})')


    # Além disso, também definir os classificados para as semifinais em novas vaiáveis:
    classificados_na_quartas = {}
    classificados_na_quartas[1] = [chaveamento_quartas_finais_1_2]
    classificados_na_quartas[2] = [chaveamento_quartas_finais_3_4]
    classificados_na_quartas[3] = [chaveamento_quartas_finais_5_6]
    classificados_na_quartas[4] = [chaveamento_quartas_finais_7_8]    
    
    # TODO : Imprimir os " resultados " dos confrontos realizados nas Quartas de Final:    
    classificados_para_semifinal(classificados_na_quartas)
    resultado_classificacao_semifinal(classificados_na_quartas)
    simulando_confrontos_semifinal(classificados_na_quartas)

    return 0 

def classificados_para_semifinal(classificados):
    print("-"*50)
    print("Os classificados para semifinal")
    for chave, selecoes_motivadas in classificados.items():
        print(f"Classificado {chave}: ", end="")
        i=0
        for selecao_motivada in selecoes_motivadas:
            print(f"{selecao_motivada.selecao} ", end="")
        print()

def confrontos_da_semifinal(classificados):
    print("-"*50)
    print("Os confrontos da semifinal")
    
    print(f'1ª SEMIFINAL: {classificados[1][0].selecao} ({classificados[1][0].ultimaMotivacao:.2f}) X {classificados[3][0].selecao} ({classificados[3][0].ultimaMotivacao:.2f})')
    print(f'2ª SEMIFINAL: {classificados[2][0].selecao} ({classificados[2][0].ultimaMotivacao:.2f}) X {classificados[4][0].selecao} ({classificados[4][0].ultimaMotivacao:.2f})')
  

def resultado_classificacao_semifinal(classificacao):
    # TODO : Imprimir os grupos , ordenados pelas melhores seleções de cada (apenas 2 se classificam)
    # Simulação da Tabela final dos confrontos das seleções nas fases de grupo
    print("-"*50)
    print("Simulação da tabela final dos confrontos das seleções para chegar as semifinais com a pontuação")
    for grupo, selecoes_motivadas in classificacao.items():
        print(f"GRUPO {grupo}: ", end="")
        for selecao_motivada in selecoes_motivadas:
            print(f"{selecao_motivada.selecao} - Última motivação: ({selecao_motivada.ultimaMotivacao:.2f}) ", end="")
        print()

    confrontos_da_semifinal(classificacao)

def simulando_confrontos_semifinal(classificados):
    # TODO : Simular os confrontos das Semifinais (randomizando novamente suas respectivas motivações).
    # Além disso, também definir os classificados para a final e disputa de 3º e 4º em novas vaiáveis:
    semifinalista1 = classificados[1][0]
    semifinalista2 = classificados[2][0]
    semifinalista3 = classificados[3][0]
    semifinalista4 = classificados[4][0]
    
    semifinal1 = semifinalista1 if semifinalista1.motivacao_para_o_time_para_a_partida() > semifinalista3.motivacao_para_o_time_para_a_partida() else semifinalista3
    semifinal2 = semifinalista2 if semifinalista2.motivacao_para_o_time_para_a_partida() > semifinalista4.motivacao_para_o_time_para_a_partida() else semifinalista4
        
    # TODO : Imprimir os " resultados " dos confrontos realizados nas Semifinais:
    confrontos_da_final(semifinal1,semifinal2)
    simulando_confronto_final(semifinal1,semifinal2)
    return 0

def confrontos_da_final(finalista1,finalista2):
    print("-"*50)
    print("Os confrontos da FINAL")
    print(f'{finalista1.selecao} X {finalista2.selecao}')    

def simulando_confronto_final(finalista1,finalista2):
    # TODO : Simular os confrontos das Finais (randomizando novamente suas respectivas motivações) .
    # Além disso, também definir os 4 primeiros colocamos da Copa do Mundo de 2022:
    campeao = finalista1 if finalista1.motivacao_para_o_time_para_a_partida() > finalista2.motivacao_para_o_time_para_a_partida() else finalista2
    o_grande_campeao_da_copa_do_mundo(campeao)

    return 0

def o_grande_campeao_da_copa_do_mundo(campeao):
    print("-"*50)
    print("O GRANDE CAMPEÃO DA COPA DO MUNDO DE 2022 NO CATAR É:")
    print(f'{campeao.selecao}')    
    print("-"*50)



if __name__ == "__main__":    
    simulando_confrontos_fase_de_grupos()