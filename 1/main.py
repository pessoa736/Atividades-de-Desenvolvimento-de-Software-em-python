
notas = []

def addnotas (nota):
    notas.append(int(nota))

def fazerMedia():
    sum = 0
    for i in notas:
        sum += i/len(notas)
    
    return sum


addnotas(input("coloque sua primeira nota:\n "))
addnotas(input("coloque sua segunda nota:\n "))
addnotas(input("coloque sua terceira nota:\n "))
addnotas(input("coloque sua quarta nota:\n "))


media = fazerMedia()

print("sua media foi ", fazerMedia())


if media>7: print("vc passou")
elif media>5: print("ficou em recupeção")
else: print("foi reprovado")




