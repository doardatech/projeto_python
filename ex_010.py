#010 Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 5.46
euro = real / 5.84
print('Com R${} você pode comprar\n'
      f'R${real:.2f} / US${dolar:.2f}\n'
      f'R${real:.2f} / EUR&{euro:.2f}\n')