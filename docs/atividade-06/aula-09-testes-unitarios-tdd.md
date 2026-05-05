# Aula 9 – Testes Unitários e TDD

## 👥 Integrantes
- Gabriel Caldeira Medeiros
- Vinicius Dobke

---

## 📁 Estrutura do Projeto

.  
├── src/  
│   ├── pedido.py  
│   ├── desconto.py  
│   └── entrega.py  
└── tests/  
    ├── test_pedido.py  
    ├── test_desconto.py  
    └── test_entrega.py  

---

## 🔹 1. Funcionalidades escolhidas

Cada integrante ficou responsável por uma regra de negócio do sistema.

---

### 👤 Gabriel Medeiros – Cálculo do total do pedido com valor mínimo

**Arquivo da implementação:** `/src/pedido.py`  
**Arquivo de testes:** `/tests/test_pedido.py`

#### Descrição
Soma os valores dos itens do pedido e valida se o total atinge o valor mínimo.

#### Regras de negócio
- Soma dos itens define o total  
- Pedido deve atingir valor mínimo  
- Caso contrário, deve gerar erro  

---

### 👤 Integrante 2 – Aplicação de desconto percentual

**Arquivo da implementação:** `/src/desconto.py`  
**Arquivo de testes:** `/tests/test_desconto.py`

#### Descrição
Aplica um desconto percentual sobre o valor total do pedido.

#### Regras de negócio
- Percentual deve estar entre 0 e 100  
- Valor final não pode ser negativo  

---

### 👤 Integrante 3 – Cálculo de taxa de entrega

**Arquivo da implementação:** `/src/entrega.py`  
**Arquivo de testes:** `/tests/test_entrega.py`

#### Descrição
Calcula a taxa de entrega com base na distância.

#### Regras de negócio
- Até 3km → taxa fixa  
- Acima de 3km → taxa adicional por km  
- Distância negativa → erro  

---

## 🔹 2. Testes Unitários

Cada integrante implementou seus testes unitários no respectivo arquivo dentro da pasta `/tests`.

---

### 🧪 Gabriel – Testes (pedido)

#### Teste 1 – Valor acima do mínimo

- Nome do teste: test_total_valido
- Cenário: Pedido com soma dos itens maior que o valor mínimo 
- Dados de entrada: itens = [{"preco": 10}, {"preco": 20}] e valor_minimo = 15
- Resultado esperado: Retornar 30 e não deve gerar erro

##### código do teste
def test_total_valido():
    itens = [{"preco": 10}, {"preco": 20}]
    resultado = calcular_total_pedido(itens, 15)
    assert resultado == 30

##### TDD
- Red: teste falhou por função inexistente  
- Green: implementação mínima  
- Refactor: cálculo real + validação  

##### Refatoração
- Substituição de valores fixos por cálculo com sum()  
- Inclusão da validação de valor mínimo 
- Código mais reutilizável e limpo

##### Execução
- Resultado: Passou  

---

#### Teste 2 – Valor abaixo do mínimo

- Nome do teste: test_total_invalido
- Cenário: Pedido com valor total menor que o valor mínimo exigido.  
- Dados de entrada: itens = [{"preco": 5}] e valor_minimo = 10
- Resultado esperado: Erro  

##### Código do teste

def test_total_invalido():
    itens = [{"preco": 5}]
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, 10)

##### TDD
- Red: teste esperando erro  
- Green: exceção implementada  
- Refactor: melhoria da validação  

##### Refatoração
- A validação foi reorganizada para melhorar a clareza e garantir que a regra de negócio fosse aplicada corretamente. 

##### Execução
- Resultado: Passou  

---

### 🧪 Integrante 2 – Testes (desconto)

#### Teste 1 – Aplicação de desconto válido

- Cenário: Desconto dentro do limite  
- Resultado esperado: Valor reduzido corretamente  

##### TDD
- Red: falha inicial  
- Green: cálculo simples  
- Refactor: validação de percentual  

##### Refatoração
- Garantia de limites do desconto  

##### Execução
- Resultado: Passou  

---

#### Teste 2 – Percentual inválido

- Cenário: Desconto maior que 100%  
- Resultado esperado: Erro  

##### TDD
- Red: falha  
- Green: validação adicionada  
- Refactor: melhoria da mensagem de erro  

##### Refatoração
- Tratamento de entrada inválida  

##### Execução
- Resultado: Passou  

---

### 🧪 Integrante 3 – Testes (entrega)

#### Teste 1 – Distância até 3km

- Cenário: Taxa fixa  
- Resultado esperado: Valor fixo  

##### TDD
- Red: falha inicial  
- Green: retorno fixo  
- Refactor: lógica condicional  

##### Refatoração
- Inclusão de regra de distância  

##### Execução
- Resultado: Passou  

---

#### Teste 2 – Distância negativa

- Cenário: Entrada inválida  
- Resultado esperado: Erro  

##### TDD
- Red: falha  
- Green: validação implementada  
- Refactor: melhoria da estrutura  

##### Refatoração
- Garantia de integridade dos dados  

##### Execução
- Resultado: Passou  

---

## 🔹 3. Reflexão

### Foi difícil escrever testes antes do código?
Sim, exige pensar primeiro na regra.

---

### O TDD ajudou no desenvolvimento?
Sim, organizou melhor o desenvolvimento.

---

### Os testes aumentaram a confiança no código?
Sim, evita regressões.

---

### O que melhorariam?
- Mais cenários extremos 
- Cobertura maior  

---

### Como isso ajuda no projeto?
Garante qualidade contínua e evolução segura.