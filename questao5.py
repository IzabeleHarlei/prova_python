x = str(input("Digite uma frase: ")) 
i1 = 0
i2 = 0
for elementos in x:
    if elementos.isalpha() == True:
        i1+=1
        print(f'Há {i1} letras')
    elif elementos.isdigit() == True:
        i2+=1
        print(f'Há {i2} números')
    
    