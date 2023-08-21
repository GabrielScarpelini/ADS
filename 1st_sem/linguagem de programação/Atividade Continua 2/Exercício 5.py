def bissexto(n):
    if n % 4 == 0 and n % 100 !=0 or n % 400 == 0: 
        return True 
    else:
        return False
begin = int(input())
end = int(input())
ano_bissexto = 0 

while begin <= end:
    if bissexto(begin):
        print(begin)
        ano_bissexto += 1
    begin += 1 

print(f'bissextos: {ano_bissexto}')
