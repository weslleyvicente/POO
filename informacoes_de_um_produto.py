nome = str(input("Qual é o nome do produto? "))
preco = float(input("Qual é o preço do produto? "))
categoria = str(input("Qual é a categoria ou o tipo do produto? "))
quantidade = int(input("Qual é a quantidade disponível em estoque? "))
validade = str(input("Qual é a data de validade? Caso Aplicável "))

print(f"Nome: {nome}, \nPreço: {preco}, \nCategoria: {categoria}, \nQuantidade: {quantidade}, \nValidade: {validade}")