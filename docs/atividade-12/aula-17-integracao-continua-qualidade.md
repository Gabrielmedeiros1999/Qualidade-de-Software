# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrantes

- Gabriel Caldeira Medeiros
- Vinicius Dobke

---

## 1. Repositório da Atividade

| Item | Descrição |
|--------|--------|
| Nome do repositório | localEats |
| Link do repositório | https://github.com/Gabrielmedeiros1999/localEats |

### Estrutura de Diretórios

```text
localEats/
├── tests/
│   ├── test_order.py
│   ├── test_order_steps.py
│   └── features/
│       └── order_total.feature
│   └── steps/
│       └── test_order_steps.py
├── .github/
│   └── workflows/
│       └── quality.yml
├── order.py
└── requirements.txt
```

---

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|--------|
| Título da Issue | Implementar cálculo do valor total do pedido |
| Objetivo da funcionalidade | Calcular automaticamente a soma dos itens do pedido |
| Link da Issue | https://github.com/Gabrielmedeiros1999/localEats/issues/1 |

---

## 3. Teste Automatizado

| Item | Descrição |
|--------|--------|
| Tipo de teste | Unitário |
| Objetivo do teste | Verificar o cálculo correto do valor total |
| Link para o arquivo do teste | https://github.com/Gabrielmedeiros1999/localEats/blob/main/tests/test_order.py |

```python
from order import calculate_total, apply_discount


def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60


def test_calculate_total_lista_vazia():
    assert calculate_total([]) == 0

def test_apply_discount():
    assert apply_discount(100, 10) == 90
```

---

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|--------|
| Nome do workflow | Quality Check |
| Evento que dispara a execução | push e pull_request |
| Link para o workflow | https://github.com/Gabrielmedeiros1999/localEats/blob/main/.github/workflows/quality.yml |
| Link da execução | https://github.com/Gabrielmedeiros1999/localEats/actions |

```yaml
name: Quality Check

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependencias
        run: |
          pip install pytest
          pip install pytest-bdd
          pip install pytest-cov

      - name: Executar testes
        run: pytest

      - name: Verificar cobertura
        run: pytest --cov=. --cov-fail-under=80
```

---

## 5. Indicadores de Qualidade

| Indicador | Valor |
|------------|---------|
| Quantidade de testes executados | 5 |
| Quantidade de testes aprovados | 5 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | passed |

## Análise dos Resultados

O pipeline de Integração Contínua foi configurado utilizando GitHub Actions para executar automaticamente os testes a cada *push* ou *pull request*. Durante a execução do pipeline, foram executados cinco testes automatizados, todos aprovados com sucesso, sem ocorrência de falhas. Esse resultado demonstra que a funcionalidade implementada atende aos cenários de teste definidos e que o código encontra-se estável para integração ao projeto principal. A utilização dos testes automatizados e do pipeline de Integração Contínua contribuiu para a validação contínua da qualidade do software, garantindo maior confiabilidade no processo de desenvolvimento e reduzindo o risco de introdução de erros em novas alterações.
