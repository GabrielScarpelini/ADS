USE DB_VENDAS

 -- SELECIONAR TODOS OS REGISTROS  
 SELECT *
 FROM TB_CLIENTE


 --SELECIONANDO ALGUMAS COLUNAS 
 SELECT 
	NOME,
	CIDADE
FROM TB_CLIENTE 

-- APELIDANDO COLUNA
SELECT
	NOME	AS CLIENTE,
	CIDADE  AS MUNICIPIO
FROM TB_CLIENTE 

SELECT
	CODFUN			[C�DIGO DO EMPREGADO],
	NOME			EMPREGADO,
	SALARIO			"SAL�RIO ATUAL",-- ASPAS DUPLAS, MESMA FUN��O DO COCHETES
	SALARIO * 1.1	'SAL�RIO REAJUSTADO' 
FROM TB_EMPREGADO

SELECT
	TB_EMPREGADO.NOME,
	TB_EMPREGADO.DATA_NASCIMENTO
FROM TB_EMPREGADO

SELECT
	EMP.NOME,
	EMP.DATA_NASCIMENTO
FROM TB_EMPREGADO AS EMP --AS � OPCIONAL 