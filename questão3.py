x = str (input("Digite um texto qualquer: "))
lista = [x]
i = 0
for letras in x:
    if letras.isalpha():
        i+=1
    print(f"Há {i} letras no texto")



