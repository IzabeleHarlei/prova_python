provas = {"João":7, "Maria":5, "Gabriela":9}
aprovados = []
for alunos,notas in provas.items():
    if notas >= 7:
        aprovados.append(alunos)
print(aprovados)
        
        
