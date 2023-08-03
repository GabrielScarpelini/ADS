def reverter(num):
    string = '0'
    limite = num
    while limite > 0:
        resto = limite % 10
        limite = limite // 10
        string = string + str(resto)

    return int(string)

print(reverter(54798))
