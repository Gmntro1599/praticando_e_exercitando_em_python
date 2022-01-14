preço_do_produto=float(input('preço do produto:'))
desconto_ofertado=5
desconto_do_produto=(preço_do_produto*desconto_ofertado)/100
valor_do_produto_com_desconto=preço_do_produto-desconto_do_produto
print('O valor do produto será R${:.2f} com 5% de desconto'.format(valor_do_produto_com_desconto))