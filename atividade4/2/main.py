
i = 1

n = int(input("diga um numero para eu te mostrar a tabuada:\n"))
while True:
    print(str(n)+" x "+str(i)+ " = "+str(n*i))
    if i>=10:
        break
    i+=1