#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de 
#tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

x = float(input('Larguda da parede: '))
y = float(input('Altura da parede: '))
area = float(x*y)
tinta = float(area/2)
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f} m²'.format(x,y,area))
print('Para pintar essa parede, você precisarpa de {}l de tinta.'.format(tinta))