import random


num_esco = random.randrange(0, 10)
while True:
    print("-------------------------------------------------")
    n = int(input("chute um numero:\n"))
    if n == num_esco:
        print("vc acertou")
        exit()
    elif n> num_esco:
        print("n<"+str(n))
    elif n< num_esco:
        print("n>"+str(n))