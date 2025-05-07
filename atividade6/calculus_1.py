


def derivada_aproximada(f, x, h=1e-5):
   # (todo mundo adora incerteza no qual se finge de precisão)
    
    return (f(x + h) - f(x - h)) / (2 * h)


def integral_aproximada(f, a, b, n=1000):

    h = (b - a) / n
    soma = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        soma += f(a + i * h)

    return soma * h


def limite_aproximado(f, x, h=1e-5):
    #limites são só sobre chegar perto o suficiente... quem liga pro resto?
    
    return (f(x + h) + f(x - h)) / 2



def area_abaixo_curva(f, a, b):
    #preguiça é sinal de eficiência.

    return integral_aproximada(f, a, b)




def ponto_critico_aproximado(f, x_inicial, max_iter=100, tol=1e-5):
    
    x = x_inicial
    for _ in range(max_iter):
        d = derivada_aproximada(f, x)
        
        if abs(d) < tol:
            return x
          
        x -= d * 0.1

    return x  
