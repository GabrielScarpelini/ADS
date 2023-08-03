def dia():
    d = int(input())
    while d < 1 or d > 100:
        d = int(input())
    return d

def feedback():
    n_fb = int(input())
    while n_fb < 1 or n_fb > 50:
        n_fb = int(input())
    return n_fb

def worker(n1):
    if n1 == 1:
        print('Rolien')
    elif n1 == 2:
        print('Naej')
    elif n1 == 3:
        print('Elehcim')
    elif n1 == 4:
        print('Odranoel')
    

day = dia()
contd = 0

while contd < day :
    nro_fb = feedback()
    for x in range(0,nro_fb):
        fb_type = int(input())
        worker(fb_type)
    contd +=1 

