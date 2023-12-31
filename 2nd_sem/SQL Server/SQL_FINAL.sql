
CREATE TABLE TB_AERODROMO
(	
	ID					SMALLINT		IDENTITY,
	SG_AERODROMO		CHAR(4) NOT NULL,
	NM_AERODROMO		VARCHAR(100) NOT NULL,
	NM_CIDADE			VARCHAR(50),
	SG_UF				CHAR(2),
	NM_PAIS				VARCHAR(50) NOT NULL,
	NM_CONTINENTE		VARCHAR(16) NOT NULL,

	CONSTRAINT PK_TB_AERODROMO PRIMARY KEY (ID),
	CONSTRAINT UQ_SG_AERODROMO_TB_AERODROMO UNIQUE (SG_AERODROMO),
	CONSTRAINT UQ_NM_AERODROMO_TB_AERODROMO UNIQUE (NM_AERODROMO),
	CONSTRAINT CK_CONTINENTE_TB_AERODROMO 
	CHECK(NM_CONTINENTE IN('AMERICA DO SUL', 'OCEANIA', 'AMERICA DO NORTE','AMERICA CENTRAL', 'AFRICA', 'EUROPA', 'ASIA'))

)

CREATE TABLE TB_EMPRESA 
(
	ID				TINYINT		IDENTITY, 
	SG_EMPRESA		CHAR(3) NOT NULL,
	NM_EMPREA		VARCHAR(100) NOT NULL,
	DS_TIPO_EMPRESA VARCHAR(13) NOT NULL,

	CONSTRAINT PK_TB_EMPRESA PRIMARY KEY (ID),
	CONSTRAINT CK_DS_TIPO_EMPREA_TB_EMPRESA CHECK (DS_TIPO_EMPRESA IN ('BRASILEIRA','ESTRANGEIRA', 'N�O INFORMADO'))
)
CREATE TABLE TB_JUSTIFICATIVA
(
	ID					TINYINT		IDENTITY,
	SG_JUSTIFICATIVA	CHAR(2) NOT NULL,
	DS_JUSTIFICATIVA	VARCHAR(100) NOT NULL,

	CONSTRAINT PK_TB_JUSTIFICATIVA PRIMARY KEY (ID),
	CONSTRAINT UQ_SG_JUSTIFICATIVA_TB_JUSTIFICATIVA UNIQUE (SG_JUSTIFICATIVA)
)
CREATE TABLE TB_TIPO_LINHA
(
	ID						TINYINT		IDENTITY,
	CD_TIPO_LINHA			CHAR(1) NOT NULL,
	DS_SERVICO_TIPO_LINHA	VARCHAR(9) NOT NULL,
	DS_NATUREZA_TIPO_LINHA  VARCHAR(13) NOT NULL,

	CONSTRAINT PK_TB_TIPO_LINHA PRIMARY KEY (ID),
	CONSTRAINT UQ_CD_TIPO_LINHA_TB_TIPO_LINHA UNIQUE (CD_TIPO_LINHA),
	CONSTRAINT CK_CD_TIPO_LINHA CHECK (CD_TIPO_LINHA IN ('N', 'C', 'I', 'G')),
	CONSTRAINT CK_DS_SERVICO_TIPO_LINHA CHECK (DS_SERVICO_TIPO_LINHA IN ('MISTA', 'CARGUEIRA')),
	CONSTRAINT CK_DS_NATUREZA_TIPO_LINHA_TB_TIPO_LINHA 
	CHECK (DS_NATUREZA_TIPO_LINHA IN ('INTERNACIONAL', 'DOM�STICA'))

)
CREATE TABLE TB_TIPO_VOO 
(
	ID						TINYINT		IDENTITY,
	DS_TIPO_VOO				VARCHAR(17) NOT NULL,
	DS_CLASSIFICACAO_VOO	VARCHAR(11) NOT NULL,

	CONSTRAINT PK_TB_TIPO_VOO PRIMARY KEY (ID),
	CONSTRAINT UQ_DS_TIPO_VOO_TB_TIPO_VOO UNIQUE (DS_TIPO_VOO),
	CONSTRAINT CK_DS_TIPO_VOO_TB_TIPO_VOO 
	CHECK (DS_TIPO_VOO IN('REGULAR', 'EXTRA', 'RETORNO',
	'INCLUS�O DE ETAPA', 'N�O REMUNERADO', 'FRETAMENTO', 'CHARTER')),
	CONSTRAINT CK_DS_CLASSIFICACAO_VOO_TB_TIPO_VOO
	CHECK (DS_CLASSIFICACAO_VOO IN('REGULAR', 'N�O REGULAR', 'IMPRODUTIVO'))
)

CREATE TABLE TB_VOO
(
    ID_VOO						INT				IDENTITY,
    ID_EMPRESA					TINYINT			NOT NULL,
    NR_VOO                      VARCHAR(4),
    ID_TIPO_VOO					TINYINT			NOT NULL,
    ID_TIPO_LINHA				TINYINT			NOT NULL,
    ID_AERODROMO_ORIGEM			SMALLINT		NOT NULL,
    ID_AERODROMO_DESTINO		SMALLINT		NOT NULL,
    DT_HR_PARTIDA_PREVISTA		DATETIME		NOT NULL,
    DT_HR_PARTIDA_REAL			DATETIME				,
    DT_HR_CHEGADA_PREVISTA		DATETIME		NOT NULL,
    DT_HR_CHEGADA_REAL			DATETIME				,
    FL_SITUACAO					CHAR(1)			NOT NULL,
    ID_JUSTIFICATIVA			TINYINT					,

	CONSTRAINT PK_TB_VOO PRIMARY KEY (ID_VOO),
	
	CONSTRAINT FK_TB_VOO_TB_EMPRESA FOREIGN KEY (ID_EMPRESA) 
	REFERENCES TB_EMPRESA(ID),

	CONSTRAINT FK_TB_VOO_TB_TIPO_VOO FOREIGN KEY (ID_TIPO_VOO)
	REFERENCES TB_TIPO_VOO (ID),

	CONSTRAINT FK_TB_VOO_TB_TIPO_LINHA FOREIGN KEY(ID_TIPO_LINHA)
	REFERENCES TB_TIPO_LINHA(ID),

	CONSTRAINT FK_TB_VOO_TB_AERODROMO_ORIGEM FOREIGN KEY (ID_AERODROMO_ORIGEM)
	REFERENCES TB_AERODROMO(ID),

	CONSTRAINT FK_TB_VOO_TB_AERODROMO_DESTINO FOREIGN KEY (ID_AERODROMO_DESTINO)
	REFERENCES TB_AERODROMO(ID),

	CONSTRAINT FK_TB_VOO_ID_JUSTIFICATIVA FOREIGN KEY (ID_JUSTIFICATIVA)
	REFERENCES TB_JUSTIFICATIVA(ID),

	CONSTRAINT CK_DT_HR_PARTIDA_REAL CHECK (DT_HR_PARTIDA_REAL < DT_HR_CHEGADA_REAL),

	CONSTRAINT CK_FL_SITUACAO CHECK (FL_SITUACAO IN('0', '1')),
)
