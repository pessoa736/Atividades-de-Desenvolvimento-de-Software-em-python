

def LitroToMililtro(litro):
    return litro*1000

for i in range(10, 100):
    if i%10 == 0:
        print(str(i/50)+" litros sâo "+str(LitroToMililtro(i/50))+" mililitro")
