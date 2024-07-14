#008 Leia um valor em metros e o exiba convertido em centímetros e milímetros.
medida = float(input('Uma distância em metros:'))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
km = medida / 1000
hm = medida / 100
dam = medida / 10
print(f'A medida de {medida}m corresponde a\n'
      f'{medida * 100:.0f}cm\n'
      f'{medida * 1000:.0f}mm\n'
      f'{medida * 10:.0f}dm\n'
      f'{medida / 1000}km\n'
      f'{medida / 100}hm\n'
      f'{medida / 10}dam\n')