# enumerate em python

collection = ['eu', 'tu', "ele"]

for value in collection:
    pass

mapping = {}
for i, value in enumerate(collection):
    mapping[value] = i

print(list(enumerate(collection)))
print(mapping)



seq1 = ["1", "2", "3"]
seq2 = ["4", "5", "6"]
seq3 = [True, False]

zipped = list(zip(seq1, seq2))

zipped2 = list(zip(seq1, seq2, seq3))
# print(zipped)
# print(zipped2)

for i, (a,b) in enumerate(zip(seq1, seq2)):
    print("index:{0} e val-lista: {1} e val-list2:{2}".format(i, a, b))

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
print(d1)