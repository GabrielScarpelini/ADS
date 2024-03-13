# enumerate em python

# tudo que tiver print é exemplo

collection = ['eu', 'tu', "ele"]

for value in collection:
    pass

mapping = {}
# for i, value in enumerate(collection):
#     mapping[value] = i

# print(list(enumerate(collection)))
# print(mapping)



seq1 = ["1", "2", "3"]
seq2 = ["4", "5", "6"]
seq3 = [True, False]

zipped = list(zip(seq1, seq2))

zipped2 = list(zip(seq1, seq2, seq3))
# print(zipped),
# print(zipped2)

for i, (a,b) in enumerate(zip(seq1, seq2)):
    # print("index:{0} e val-lista: {1} e val-list2:{2}".format(i, a, b))
    pass

pessoas = [("nolan", "ryan"), ("roger", "clems"), ("sandy","curt")]

# * descompacta a tupla
nomes, pessoas = zip(*pessoas)

# jogar no dicionário

d1 = {"A": "value", "B": [0,1,2,3]}

d1[5] = "valor"
del d1[5]

d1.pop("A")


# print(d1[5])

# print(d1["A"])
# print(d1)

# print(list(d1.values()))
# print(d1.values())


d1.update({"B": [9,8,7,6], 5: "Preço"})
# print(d1)

listKeys = ["Gabriel", "Theiago", "Thiago"]
listValues = ["Skarpa", "Laguin", "Roznado"]

for key, value in zip(listKeys, listValues):
    mapping[key] = value


mappin2 = dict(zip(listKeys, listValues))

# print(mapping)
# print(mappin2)


# list, dict comprehensions

condiction = 3>=0
expression = 0

[expression for val in collection if condiction]
# SÃO IGUAIS ESSES DOIS, MAS UM É UM FOR DE UMA LINHA.
result = []

for val in collection:
    if condiction:
        result.append(expression)

string = ["eu", "tu", "ele"]

# samples 
# print([x.upper() for x in string])
# print([x.upper() for x in string if len(x)>2])

locMap = {val : index for index, val in enumerate(string)}

# print(locMap)

allData = [["JOÂO", "Maria"],
           ["JOHN", "Mary"]]

interestNames = []

for names in allData:
    enoughA = [name for name in nomes if name.count("a") >= 2]
    interestNames.append(enoughA)

result = [name for names in allData for name in names if name.count("a") >= 2]

# print(result)

someTuple = [(1,2,3), (4,5,6), (7,8,9)]

line = [x for tup in someTuple for x in tup]


lists = [[x for x in tup] for tup in someTuple]

# print(lists)

#  em funções com valor default, o valor default vem sempre dps do args posisionais \/
def fucki(a, x, c=1):
    return c

# print(fucki(a, b))

state = ["Alabama", "havaii", "alabama", "georgia", "florida$$", "south carolina"]


import re #

def clearString(string):
    result = []
    for value in string:
        value = value.strip() #remove espaços em branco
        value = re.sub("[$!?]", "", value) # retirar os caracteres 
        result.append(value)
        return result
    
print(clearString([x for x in state]))