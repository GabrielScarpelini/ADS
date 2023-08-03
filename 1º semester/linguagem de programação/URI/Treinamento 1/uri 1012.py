'''a = input()
b = input()
c = input() 
a = float(a)
b = float(b)
c = float(c) 
pi= 3.14159
area_triangulo = (a*c)/2
area_circulo = pi * c **2
area_trapezio = ((a + b)*2)/2
area_quadrado = b * b
area_retangulo = a * b
print(f'TRIANGULO: {area_triangulo:.3f}\n'
      f'CIRCULO: {area_circulo:.3f}\n'
      f'TRAPEZIO: {area_trapezio:.3f}\n'
      f'QUADRADO: {area_quadrado:.3f}\n'
      f'RETANGULO: {area_retangulo:.3f}')
'''
a,b,c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159
area_triangulo = (a*c)/2
area_circulo = pi * c **2
area_trapezio = ((a + b)*c)/2
area_quadrado = b * b
area_retangulo = a * b
print(f'TRIANGULO: {area_triangulo:.3f}\n'
      f'CIRCULO: {area_circulo:.3f}\n'
      f'TRAPEZIO: {area_trapezio:.3f}\n'
      f'QUADRADO: {area_quadrado:.3f}\n'
      f'RETANGULO: {area_retangulo:.3f}')
