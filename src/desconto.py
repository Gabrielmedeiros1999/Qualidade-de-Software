def calcular_desconto(total_pedido):

    if total_pedido <= 0:
        raise ValueError("O valor do pedido não pode ser zero ou negativo")

    if total_pedido > 0 and total_pedido < 60:
        return total_pedido

    if total_pedido >= 60 and total_pedido < 100:
        desconto10 = total_pedido * 0.1
        return total_pedido - desconto10
    
    if total_pedido >= 100:
        desconto15 = total_pedido * 0.15
        return total_pedido - desconto15
