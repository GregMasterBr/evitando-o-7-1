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
    simulando_confrontos_oitavas_de_final(melhoresSelecoesPorGrupo)


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
              
    # TODO : Simular os confrontos das Oitavas de Final (randomizando novamente suas respectivas motivações) .
    # Além disso, também definir os classificados para as quartas de final em novas vaiáveis:    
    
    chaveamento_quartas_finais_AB_1 = team1A if team1A.motivacao_para_o_time_para_a_partida() > team2B.motivacao_para_o_time_para_a_partida() else team2B
    chaveamento_quartas_finais_AB_2 = team2A if team2A.motivacao_para_o_time_para_a_partida() > team1B.motivacao_para_o_time_para_a_partida() else team1B

    chaveamento_quartas_finais_CD_1 = team1C if team1C.motivacao_para_o_time_para_a_partida() > team2D.motivacao_para_o_time_para_a_partida() else team2D
    chaveamento_quartas_finais_CD_2 = team2C if team2C.motivacao_para_o_time_para_a_partida() > team1D.motivacao_para_o_time_para_a_partida() else team1D

    chaveamento_quartas_finais_EF_1 = team1E if team1E.motivacao_para_o_time_para_a_partida() > team2F.motivacao_para_o_time_para_a_partida() else team2F
    chaveamento_quartas_finais_EF_2 = team2E if team2E.motivacao_para_o_time_para_a_partida() > team1F.motivacao_para_o_time_para_a_partida() else team1F

    chaveamento_quartas_finais_GH_1 = team1G if team1G.motivacao_para_o_time_para_a_partida() > team2H.motivacao_para_o_time_para_a_partida() else team2H
    chaveamento_quartas_finais_GH_2 = team2G if team2G.motivacao_para_o_time_para_a_partida() > team1H.motivacao_para_o_time_para_a_partida() else team1H
    
    classificados_na_oitavas = {}

    classificados_na_oitavas[1] = [chaveamento_quartas_finais_AB_1]
    classificados_na_oitavas[2] = [chaveamento_quartas_finais_AB_2]
    classificados_na_oitavas[3] = [chaveamento_quartas_finais_CD_1]
    classificados_na_oitavas[4] = [chaveamento_quartas_finais_CD_2]
    classificados_na_oitavas[5] = [chaveamento_quartas_finais_EF_1]
    classificados_na_oitavas[6] = [chaveamento_quartas_finais_EF_2]
    classificados_na_oitavas[7] = [chaveamento_quartas_finais_GH_1]
    classificados_na_oitavas[8] = [chaveamento_quartas_finais_GH_2]

    resultado_classificacao_oitavas_de_final(classificados_na_oitavas)
    return 0

def resultado_classificacao_oitavas_de_final(classificados):
    print("-"*50)
    print("Simulação da tabela dos das seleções classificados para as Quartas de final")
    for chave, selecoes_motivadas in classificados.items():
        print(f"CHAVE {chave}: ", end="")
        for selecao_motivada in selecoes_motivadas:
            print(f"{selecao_motivada.selecao} - Última motivação: ({selecao_motivada.ultimaMotivacao:.2f}) ", end="")
        print()
    

def simulando_confrontos_quartas_de_final():
    # TODO : Simular os confrontos das Quartas de Final (randomizando novamente suas respectivas motivações).
    # Além disso, também definir os classificados para as semifinais em novas vaiáveis:
    # TODO : Imprimir os " resultados " dos confrontos realizados nas Quartas de Final:    
    
    return 0 

def simulando_confrontos_semifinal():
    # TODO : Simular os confrontos das Semifinais (randomizando novamente suas respectivas motivações).
    # Além disso, também definir os classificados para a final e disputa de 3º e 4º em novas vaiáveis:
    # TODO : Imprimir os " resultados " dos confrontos realizados nas Semifinais:

    return 0

def simulando_confronto_final():
    # TODO : Simular os confrontos das Finais (randomizando novamente suas respectivas motivações) .
    # Além disso, também definir os 4 primeiros colocamos da Copa do Mundo de 2022:

    return "BRASIL"


def criar_classe_selecao():
    pass

def campeao():
    return "Brasil"



if __name__ == "__main__":    
    simulando_confrontos_fase_de_grupos()