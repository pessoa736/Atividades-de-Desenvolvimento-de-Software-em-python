lista_compras = {}

def adicionar_item(nome, quantidade, preco):
    id = "item " + str(len(lista_compras) + 1)
    item = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    lista_compras[id] = item

def mostrar_lista():
    for item_id in lista_compras:
        st = "- " + item_id + "\n"
        for info in lista_compras[item_id]:
            st += f"\t{info}: '{lista_compras[item_id][info]}'\n"
        print(st)




adicionar_item("Arroz", 2, 5.99)
adicionar_item("Leite", 3, 3.49)
adicionar_item("Sabonete", 5, 1.99)

mostrar_lista()