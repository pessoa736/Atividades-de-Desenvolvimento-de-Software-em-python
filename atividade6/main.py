import math
import calculus_1 as c


print(
    "Derivada de x^2 em x=3 :\t", 
    c.derivada_aproximada(lambda x: x**2, 3)
)

print(
    "Derivada de sin(x) em x=π/4 :\t", 
    c.derivada_aproximada(math.sin, math.pi/4)
)

print(
    "Integral de x^2 de 0 a 1 :\t", 
    c.integral_aproximada(lambda x: x**2, 0, 1)
)

print(
    "Integral de sin(x) de 0 a π :\t", 
    c.integral_aproximada(math.sin, 0, math.pi)
)

print(
    "Limite de sin(x)/x em x=0:\t",
    c.limite_aproximado(lambda x: math.sin(x)/x if x != 0 else 1, 0)
)

print(
    "Área abaixo de x^2 entre 0 e 2:\t",
    c.area_abaixo_curva(lambda x: x**2, 0, 2)
)

print(
    "Ponto crítico de x^2 - 4x + 3:\t",
    c.ponto_critico_aproximado(lambda x: x**2 - 4*x + 3, 0)
)

