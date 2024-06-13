x = int(input("Digite quantos ítens serão adicionados: "))
lista_numeros = []
lista_texto = []
print(f"digite os {x} caracteres abaixo")
for items in range(x):
    items = input(": ")
    if items.isalpha() == True:
      lista_texto.append(items)
    elif items.isdigit() == True:
      lista_numeros.append(items)
print(f"{lista_numeros} é a lista de números")
print(f"{lista_texto} é a lista de textos")  