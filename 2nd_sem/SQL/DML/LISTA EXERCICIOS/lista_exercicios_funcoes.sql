USE DB_VENDAS 

SELECT
	NOME,
	LEFT(NOME,CHARINDEX(' ',NOME)) 							 +
	RIGHT(NOME,CHARINDEX(' ',REVERSE(NOME)))            ULTIMO_NOME
FROM TB_CLIENTE

