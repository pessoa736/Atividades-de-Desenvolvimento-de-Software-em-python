
class aluno:
    notas=[]
    nome = "aluno"
    def __init__(self, nome):
        self.nome = nome

    def addNotas(self, nota):
        self.notas.append(int(nota))
    
    def getMedia(self):
        return sum(self.notas)/len(self.notas)


clodoaldo = aluno("clodoaldo valentim")

clodoaldo.addNotas(7)
clodoaldo.addNotas(5)
clodoaldo.addNotas(6)
clodoaldo.addNotas(7)

print("a media de clodoaldo é " + str(clodoaldo.getMedia()))




