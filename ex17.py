dias=float(input('Quantos dias você usou o carro?'))
km=float(input('Quantos Kilometros você percorreu?'))
preço_por_dia=dias*60
preço_km=km*0.15
print('Você pagará R${:.2f} pelo o uso do carro'.format(preço_km+preço_por_dia))