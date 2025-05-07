def somaImposto(taxa_imposto, custo):
    return custo * (1 + (taxa_imposto / 100))

print(somaImposto(20, 198.90))