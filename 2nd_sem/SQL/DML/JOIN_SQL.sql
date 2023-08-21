USE DB_VENDAS 

-- join procura pelo ID chave estrangeira com principal (FKestado e 
-- PKestado) no Innerjoin só vai retornar o que for igual 

--EMPREGADO DEPARTAMENTO
SELECT * FROM TB_EMPREGADO
SELECT * FROM TB_DEPARTAMENTO

SELECT 
	tb_empregado.nome, 
	tb_departamento.depto
FROM TB_EMPREGADO
	INNER JOIN TB_DEPARTAMENTO
		ON TB_EMPREGADO.COD_DEPTO = TB_DEPARTAMENTO.COD_DEPTO
where tb_departamento.depto = 'c.p.d.'


-- nome do empregado, departamento e cargo 

select 
	emp.nome,
	dep.depto,
	car.cargo
from tb_empregado emp
	inner join tb_cargo car 
		on emp.cod_cargo = car.cod_cargo
	inner join tb_departamento dep
		on emp.cod_depto = dep.cod_depto

-- inner join e só join´são a mesma coisa 


-- LEFT JOIN tras a intesecção traz todos os matchs e todos da esquerda
-- mesmo que retorne ull na direita

SELECT 
	tb_empregado.*                  -- ponto é obrigatório
FROM TB_EMPREGADO
	left JOIN TB_DEPARTAMENTO
		ON TB_EMPREGADO.COD_DEPTO = TB_DEPARTAMENTO.COD_DEPTO
where tb_empregado.cod_depto is null


-- RIGHT JOIN a intesecção traz tudo e tras tudo que estiver na direita 
-- na tabela depois do join inclusive trazendo valores nulls 

-- todos os produtos, se tiver o tipo traga a descrição do tipo 

select 
	*
from TB_TIPOPRODUTO
	right join tb_produto
		on tb_tipoproduto.cod_tipo = tb_produto.cod_tipo


-- todos os tipos que não possuem produtos cadastrados 

select 
	*
from TB_TIPOPRODUTO
	right join tb_produto
		on tb_tipoproduto.cod_tipo = tb_produto.cod_tipo
where tb_produto.cod_tipo is null

-- full alter join ele tras tudo que está na direita e tudo que está na esquerda

-- nome do produto e o tipo do produto, todos os registros produto com tipo. produto sem tipo 
-- e tipo sem produto 

select 
	tb_produto.descricao as produto,
	tb_tipoproduto.tipo
from tb_produto
	full outer join tb_tipoproduto
	 on tb_produto.cod_tipo = tb_tipoproduto.cod_tipo


-- nome do produto e o tipo do produto, somente dos produtos sem tipo 
-- ow dos tipos sem produto

select 
	tb_produto.descricao as produto,
	tb_tipoproduto.tipo
from tb_produto
	full outer join tb_tipoproduto
	 on tb_produto.cod_tipo = tb_tipoproduto.cod_tipo
where tb_produto.cod_tipo is null or tb_tipoproduto.cod_tipo is null


-- cross join, pega tudo de todas as tabelas, tudo junto e misturado 

-- lista de todos os produtos de todos os clientes(ndependente de compra)

select 
	tb_cliente.nome,
	tb_produto.descricao
from tb_cliente
	cross join TB_PRODUTO