# Evitandoo o 7 a 1  
Referência a derrota do Brasil para Alemanha na Copa do Mundo no Brasil em 2014.

##Live do DIO PRO - Evitando o 7 a 1 com Python e SQL.  
[Canal youtube Digital Innovation One](https://www.youtube.com/watch?v=QM21LkNTx84 ) 
Solução da live no [Google Colab](https://bit.ly/dio-evitando-7x1-colab)
 
## Objetivo  
Criar simulações para prever a próxima seleção campeã do mundo na copa do Catar em 2022 com a linguagem Python e estatísticas baseadas nos ranking FIFA atribuído as seleções.  

Vamos explorar um Banco de Dados Relacional (SQL) modelado com todas as seleções, grupos e critérios relevantes para a simulação das partidas


## Lógica
Será feita todas as rodadas baseadas nos confrontos em grupo, oitavas de final, quarta de final, semifinal e final.

* Todas as seleções participantes da Copa do Mundo, agrupada em seus respectivos grupos de sorteio.  
1. Grupo A 
Qatar, Equador, Senegal e Holanda 

2. Grupo B 
Inglaterra, RI do Irã, Estados Unidos e País de Gales 

3. Grupo C 
Argentina, Arábia Saudita, México e Polônia 

4. Grupo D 
França, Austrália, Dinamarca e Tunísia 

5. Grupo E 
Espanha, Costa Rica, Alemanha e Japão

6. Grupo F 
Bélgica, Canadá, Marrocos e Croácia 

7. Grupo G 
Brasil, Sérvia, Suíça e Camarões 

8. Grupo H 
Portugal, Gana, Uruguai e República da Coreia 


### Uso das informações do Ranking da Fifa para cada seleção.  
Hoje o Brasil lidera o ranking, tendo maior probabilidade de vencer o torneio.  
[Top 10 do novo ranking da Fifa](https://placar.abril.com.br/copa-do-mundo/ranking-da-fifa-brasil-segue-lider-e-argentina-passa-a-franca/):

1. Brasil – 1.837,56 pontos
2. Bélgica – 1.821,92
3. Argentina – 1.770,65
4. França – 1.764,85
5. Inglaterra – 1.737,46
6. Espanha – 1.716,93
7. Itália – 1.713,86
8. Holanda – 1.679,41
9. Portugal – 1.678,65
10. Dinamarca – 1.665,47 
11. Alemanha – 1659,0
12.	México	– 1649,6
13.	Uruguai	– 1641,0	
14.	Estados – Unidos	1635,0
15.	Croácia	– 1632,2
16.	Suíça	– 1621,4
17.	Colômbia –	1604,1
18.	Senegal	– 1584,6
19.	País de Gales	– 1582,1
20.	Suécia	– 1563,4

#### Sistema de formação do Ranking 
Este Ranking mensal elaborado pela FIFA, é baseado num sistema de pontuação que tem em conta os resultados das Seleções Nacionais nos últimos quatro anos, com um peso porcentual de 100 %, 50 %, 30 %, 20 %.  

Cada vitória (três pontos) ou empate (um ponto) é então multiplicado por vários fatores que influenciam o valor final, valor esse que será o utilizado para efeitos de Ranking.  

Assim os restantes fatores são:  

a) Importância do jogo
* Amistoso: 1.0
* Eliminatórias para competições continentais, ou mundiais: 2.5
* Torneios continentais/Copa das Confederações: 3
* Jogo de Copa do Mundo: 4.0


b) Força do adversário
Depende da colocação no ranking e é baseada na seguinte fórmula: 200 menos a posição no último ranking divulgado. Exemplos: o vice-líder vale 198, o terceiro 197, o décimo 190, e por ai em diante.
A regra tem duas exceções: o líder vale sempre 200 e a força mínima é de 50 para os países que estiverem abaixo da posição 150.

c) Força regional
As confederações não tem todas o mesmo peso, ou dificuldade. Como cerca de 85% das partidas são entre equipes da mesma confederação, seria desequilibrado deixar um jogo da Oceânia valer o mesmo que uma partida entre continentes ou dentro da Europa, por exemplo. Então, a partir de um cálculo feito analisando os jogos dos membros de uma confederação contra outras nas últimas três Copas do Mundo, o ranking concedeu a seguinte pontuação:

1. UEFA – 1.0
2. CONMEBOL – 1.0
3. CONCACAF – 0.88
4. AFC – 0.86
5. CAF – 0.86
6. OFC – 0.85

**Fonte: [FIFA](https://www.fifa.com/fifa-world-ranking/men?dateId=id13750)**