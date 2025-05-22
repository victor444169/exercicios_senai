# passo 1 : (produto) pedir para o usuário informar o produto
# passo 2 : (valor_total) pedir para o usuário informar o valor total
# passo 3 : (porcentagem) pedir para o usuário informar a porcentagem de desconto

# passo 4 : (desconto) calcular o desconto ->>  valor_total * (porcentagem / 100)

# passo 5 : (valor_novo) calcular o valor com desconto ->> valor_total - desconto

# passo 6 : Mostrar na tela o valor


produto = input('informe o produto: ')
valor_total = float(input('informe o valor total: '))
porcentagem = float(input('informe a porcentagem de desconto: '))

desconto = valor_total * (porcentagem / 100)
valor_novo = valor_total - desconto


# print('O', produto, 'com', porcentagem, '% de desconto custará: R$ ', valor_novo)
print(f'o {produto} com {porcentagem} % de desconto custará R$ {valor_novo}')


