import pytest 
from src.frete import calcular_frete

def test_menor_frete():
    valorFrete = calcular_frete(3)
    assert valorFrete == 8

def test_frete_proporcional():
    valorFrete = calcular_frete(3.1)
    assert valorFrete == 9.5

def test_distancia_invalida():
    with pytest.raises(ValueError):
        calcular_frete(-0.1)