import pytest 
from src.desconto import calcular_desconto

def test_sem_desconto():
    valorFinal = calcular_desconto(59)
    assert valorFinal == 59

def test_desconto10():
    valorFinal = calcular_desconto(60)
    assert valorFinal == 54

def test_desconto15():
    valorFinal = calcular_desconto(100)
    assert valorFinal == 85

def test_desconto_limiar_entre_10_e_15():
    valorFinal = calcular_desconto(99)
    assert valorFinal == 89.1

def test_receber_valor_zero():
    with pytest.raises(ValueError):
        calcular_desconto(0)

def test_receber_valor_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(-1)