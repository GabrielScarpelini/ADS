import os.path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

%matplotlib inline

# Modifique o diretório para fazer a leitura dos dados em dados_banco.csv

# Dados banco - Leitura dos dados
# Caso necessário, leia a partir de um diretório da sua máquina
# dados = pd.read_csv(f'{pkgdir}/dados_banco.csv', index_col=0)

# Se usar o colab, faça o upload do arquivo dadso_banco.csv
dados = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/dados_banco.csv', index_col=0)

#dados.head()
#tail mostra as ultimas columnas