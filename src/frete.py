def calcular_frete(distancia):
    
    if distancia < 0:
        raise ValueError("A distância não pode ser negativa")
    
    if distancia >= 0 and distancia <= 3:
        return 8

    if distancia > 3:
        taxaExtra = (round(distancia) / 2)
        return 8 + taxaExtra