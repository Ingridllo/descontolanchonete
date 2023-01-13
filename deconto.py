print('Bem vindo a loja Como mais e Pago menos ')
valororiginal = float( input('Entre com o Valor do Produto: R$ ') )
quantidade = int(input('Entre com a quantidade do produto?'))
if 0 <= quantidade < 10:
 desconto = 0
elif 10 <= quantidade < 100:
 desconto = 0.5

elif 100 <= quantidade < 1000:
 desconto = 0.10
else:
 desconto = 0.15
Semdesconto = valororiginal * quantidade
Comdesconto = Semdesconto - Semdesconto * desconto
print('O valor Sem desconto foi R${:.2f}'. format(Semdesconto))
print('O valor Com desconto foi R${:.2f}' . format(Comdesconto, desconto))
print('Tenha um Excelente dia...')
