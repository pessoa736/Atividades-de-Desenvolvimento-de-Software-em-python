class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        from math import pi
        return pi * self.raio ** 2

    def circunferencia(self):
        from math import pi
        return 2 * pi * self.raio
    
Ca = Circulo(2)

print(Ca.area())
print(Ca.circunferencia())

Cb = Circulo(10)

print(Cb.area())
print(Cb.circunferencia())

Cc = Circulo(1)

print(Cc.area())
print(Cc.circunferencia())