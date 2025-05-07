def valorPagamento(valor, dias_atraso):
    if dias_atraso == 0:
        return valor
    else:
        multa = valor * 0.03
        juros = valor * 0.001 * dias_atraso
        return valor + multa + juros

def loopPrestacoes():
    total = 0
    quantidade = 0
    while True:
        valor = float(input("Informe o valor da prestação (0 para sair): "))
        if valor == 0:
            break
        dias = int(input("Informe os dias de atraso: "))
        valor_final = valorPagamento(valor, dias)
        print(f"Valor a pagar: R${valor_final:.2f}")
        total += valor_final
        quantidade += 1
    print(f"\nRelatório do dia:")
    print(f"Total de prestações pagas: {quantidade}")
    print(f"Valor total pago: R${total:.2f}")


loopPrestacoes()