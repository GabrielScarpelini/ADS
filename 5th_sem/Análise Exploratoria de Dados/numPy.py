import numpy as np

myApp = np.arange(100)

# print(myApp)

# %time for _ in range(10): myArr = myApp**2

data = np.random.randn(3,2) # cada linha é um index da lista que gera é random por conta do 
# print(data)

# print(data*10) #aqui ele multiplica todos os indices da matriz

# print(data[0]) #aqui ele multiplica todos os indices da matriz
# print(data[0]* data[0][0])
# print(data[0]+ 100)


# print(data.shape) #mosta como foi criada a matriz 
# print(data.ndim) #número de linhas

data1 = [1,3,5,7,9,11]

arr1 = np.array(data1)

print(arr1.dtype)

# print(arr1)

numString = np.array(["1.5", "4.45", "8.54", "3.65"])
print(numString.dtype)
print(numString.astype(float))

print(3**0.5) # raiz quadrada

