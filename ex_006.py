#006  Leia um número e mostre seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'O dobro de {n} vale {n*2}.O triplo de {n} vale {n*3}. A raiz quadrada de {n} vale {n**(1/2):.2f}')