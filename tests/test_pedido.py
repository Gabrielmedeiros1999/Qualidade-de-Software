import pytest
from src.pedido import calcular_total_pedido


def test_total_valido():
    itens = [{"preco": 10}, {"preco": 20}]
    resultado = calcular_total_pedido(itens, 15)
    assert resultado == 30


def test_total_igual_minimo():
    itens = [{"preco": 10}, {"preco": 5}]
    resultado = calcular_total_pedido(itens, 15)
    assert resultado == 15


def test_total_invalido():
    itens = [{"preco": 5}]
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, 10)