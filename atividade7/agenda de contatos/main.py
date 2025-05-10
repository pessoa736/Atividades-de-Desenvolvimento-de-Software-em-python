
contatos = {}

def addContato(nome, telefone, email):
    id = "contatos " + str(len(contatos)+1)
    
    contato={
            "nome": nome,
            "telefone": telefone,
            "email":  email
        }

    contatos[id] = contato

def showContatos():
    for c in contatos:
        st = "- " + c + " \n" 
        for info in contatos[c]:
            st = st + "\t" + info + ": '" + str(contatos[c][info]) + "'\n"
        print(st)
    


addContato( "skibidi toilet", "(69) 96969-6969", "skibidi@sex.free")
addContato( "aaaaaaaaaaaaaa", "(00) 00000-0001", "_@__.__")


showContatos()