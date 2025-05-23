
peso = float(input('qual o seu peso? '))
altura = float(input('qual a sua altura? '))
imc = peso / (altura * altura )

resultado = round(imc, 2)
print(resultado)

if resultado >=30:
    print('toma cuidado com a sua saude, se cuide!')

else:
    print('tudo ok com a sua saude!')

