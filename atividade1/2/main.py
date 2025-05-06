
notas = []

def addnotas (nota):
    notas.append(int(nota))

def fazerMedia():
    sum = 0
    for i in notas:
        sum += i/len(notas)
    
    return sum

nome = input("qual é seu nome????????????????????????????????????????????????????????????????\n")
addnotas(input("coloque sua primeira nota:\n "))
addnotas(input("coloque sua segunda nota:\n "))
addnotas(input("coloque sua terceira nota:\n "))
addnotas(input("coloque sua quarta nota:\n "))



media = fazerMedia()

print("sua media foi ", fazerMedia())


if media>70: print(nome,"vc passou")
elif media>60: print(nome, "ficou em recupeção")
else: print(nome,"foi reprovado")




