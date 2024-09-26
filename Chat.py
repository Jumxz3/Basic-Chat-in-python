import os

mensagens = []
nome = input("Nome:")

while True:
    #limpar terminal
    os.system("cls")

    if len(mensagens) > 0:
        for m in mensagens:
            print( m["nome"], "-", m["texto"] )
    
    print("_____________")

    # Obtendo texto
    texto = input("Mensagem: ")
    if texto == "fim":
        break
    # Add mensagens na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })