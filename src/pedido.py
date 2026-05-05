def calcular_total_pedido(itens, valor_minimo):
    if not itens:
        raise ValueError("Pedido deve ter pelo menos um item")

    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total