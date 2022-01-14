import math
cateto_oposto=float(input('Cateto oposto:'))
cateto_adjacente=float(input('Cateto adjacente:'))
hipotenusa=math.hypot(cateto_oposto,cateto_adjacente)
print('A hipotenusa é igual a {:.2f}'.format(hipotenusa))
