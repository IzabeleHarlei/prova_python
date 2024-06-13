quant_num= int(input("Diga quntos ítens você deseja adicionar a lista de números: "))
lista_posi = []
lista_neg = []
for num in range(quant_num):
  num=int(input("digite um numero:"))
  if num > 0:
    lista_posi.append(num)
  else:
    lista_neg.append(num)

print(f'{lista_posi} é a lista dos números positivos')
print(f"{lista_neg} é a lista dos números negativos")