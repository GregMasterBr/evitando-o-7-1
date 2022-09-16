SELECT g.NOME AS Grupo, t.NOME AS Seleção, t.SCORE AS Pontuação
		FROM GRUPOS AS g INNER JOIN TIMES AS t 
        ON (g.ID = t.ID_GRUPO) 
        ORDER BY g.nome,t.SCORE DESC;