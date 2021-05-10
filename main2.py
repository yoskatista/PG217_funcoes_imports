def funcao(dinheiro):
    print("Você tem " + str(dinheiro) + " na carteira")

def pizza(saldo_conta, *pedidos):
    print("\nDe saldo temos R$" + str(saldo_conta) + ".")
    for pedido in pedidos:
        print("Você pediu: " + pedido)
