def converterHora(hora24, minuto):
    if hora24 == 0:
        return 12, minuto, 'A'
    elif 1 <= hora24 < 12:
        return hora24, minuto, 'A'
    elif hora24 == 12:
        return 12, minuto, 'P'
    else:
        return hora24 - 12, minuto, 'P'



def mostrarHora(hora, minuto, periodo):
    print(f"{hora}:{minuto:02d} {'A.M.' if periodo == 'A' else 'P.M.'}")



def loop_conversao_hora():
    while True:
        h = int(input("Digite a hora (0-23): "))
        m = int(input("Digite os minutos (0-59): "))
        
        hora12, minuto, periodo = converterHora(h, m)
        mostrarHora(hora12, minuto, periodo)
        
        repetir = input("Deseja converter outra hora? (s/n): ")
        
        if repetir.lower() != 's':
            break


loop_conversao_hora()