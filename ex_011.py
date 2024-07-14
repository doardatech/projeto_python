#011 Leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg} x {alt} e sua área é de {area}m², então será necessário {area/2:.0f} litros para pintá-la.')