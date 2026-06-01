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

### 👤 Vinicius Dobke – Aplicação de desconto percentual com base no valor do pedido

**Arquivo da implementação:** `/src/desconto.py`  
**Arquivo de testes:** `/tests/test_desconto.py`

#### Descrição
Aplica um desconto percentual sobre o valor total do pedido.

#### Regras de negócio
- Valor do pedido não pode ser 0 ou negativo
---

### 👤 Vinicius Dobke – Cálculo de taxa de entrega

**Arquivo da implementação:** `/src/frete.py`  
**Arquivo de testes:** `/tests/test_frete.py`

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

### 🧪 Vinicius Dobke – Testes (desconto)

#### Teste 1 – Pedido sem desconto

- Cenário: Valor do pedido não é suficiente para receber desconto
- Resultado esperado: Valor do pedido permanece o mesmo

##### Código do Teste

def test_sem_desconto():
    valorFinal = calcular_desconto(59)
    assert valorFinal == 59

##### TDD
- Red: falha inicial  
- Green: cálculo simples  
- Refactor: melhor organização de código 

##### Refatoração
- Garantia de limites do desconto
- Melhoria da legibilidade do código

##### Execução
- Resultado: Passou  
---

#### Teste 2 – Desconto de 10% no valor do pedido

- Cenário: Valor do pedido é suficiente para um desconto de 10%
- Resultado esperado: Valor do pedido ser reduzido em 10%

##### Código do Teste

def test_desconto10():
    valorFinal = calcular_desconto(60)
    assert valorFinal == 54

##### TDD
- Red: falha  
- Green: desconto aplicado corretamente
- Refactor: aplicação de princípios de código limpo

##### Refatoração
- Melhoria na legibilidade do código

##### Execução
- Resultado: Passou  
---

#### Teste 3 – Desconto de 15% no valor do pedido

- Cenário: Valor do pedido é suficiente para um desconto de 15%
- Resultado esperado: Valor do pedido ser reduzido em 15%

##### Código do Teste

def test_desconto15():
    valorFinal = calcular_desconto(100)
    assert valorFinal == 85

##### TDD
- Red: falha  
- Green: desconto aplicado corretamente
- Refactor: aplicação de princípios de código limpo

##### Refatoração
- Melhoria na legibilidade do código  

##### Execução
- Resultado: Passou  
---

#### Teste 4 – Verificação do limiar entre os descontos de 10% e 15%

- Cenário: Valor do pedido está na divisa entre os valores para desconto de 10% e 15%
- Resultado esperado: Valor do pedido sera reduzido em 10%

##### Código do Teste

def test_desconto_limiar_entre_10_e_15():
    valorFinal = calcular_desconto(99)
    assert valorFinal == 89.1

##### TDD
- Red: falha  
- Green: desconto aplicado corretamente
- Refactor: aplicação de princípios de código limpo

##### Refatoração
- Melhoria na legibilidade do código  

##### Execução
- Resultado: Passou  
---

#### Teste 5 – Valor do pedido é 0

- Cenário: Valor do pedido é zero
- Resultado esperado: A função retorna erro

##### Código do Teste

def test_receber_valor_zero():
    with pytest.raises(ValueError):
        calcular_desconto(0)

##### TDD
- Red: falha  
- Green: a funcionalidade retorna erro
- Refactor: aplicação de princípios de código limpo

##### Refatoração
- Melhoria na legibilidade do código  

##### Execução
- Resultado: Passou  
---

#### Teste 6 – Valor do pedido é negativo

- Cenário: Valor do pedido é negativo
- Resultado esperado: A função retorna erro

##### Código do Teste

def test_receber_valor_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(-1)

##### TDD
- Red: falha  
- Green: a funcionalidade retorna erro
- Refactor: aplicação de princípios de código limpo

##### Refatoração
- Melhoria na legibilidade do código  

##### Execução
- Resultado: Passou  
---

### 🧪 Vinicius Dobke – Testes (frete)

#### Teste 1 – Taxa fixa

- Cenário: Distãncia é menor do que 3km
- Resultado esperado: A taxa de entrega é fixa

##### Código do Teste

def test_menor_frete():
    valorFrete = calcular_frete(3)
    assert valorFrete == 8

##### TDD
- Red: falha  
- Green: o valor da taxa é fixa
- Refactor: aplicação de princípios de código limpo

##### Refatoração
- Melhoria na legibilidade do código  

##### Execução
- Resultado: Passou  
---

#### Teste 2 – Taxa proporcional

- Cenário: Distãncia é maior do que 3km
- Resultado esperado: A taxa de entrega aumenta conforme a distância

##### Código do Teste

def test_frete_proporcional():
    valorFrete = calcular_frete(3.1)
    assert valorFrete == 9.5

##### TDD
- Red: falha  
- Green: o valor da taxa é proporcional
- Refactor: aplicação de princípios de código limpo

##### Refatoração
- Melhoria na legibilidade do código  

##### Execução
- Resultado: Passou  
---

#### Teste 3 – Distância inválida

- Cenário: Distãncia é negativa
- Resultado esperado: A função retorna erro

##### Código do Teste

def test_distancia_invalida():
    with pytest.raises(ValueError):
        calcular_frete(-0.1)

##### TDD
- Red: falha  
- Green: a funcionalidade retorna erro
- Refactor: aplicação de princípios de código limpo

##### Refatoração
- Melhoria na legibilidade do código  

##### Execução
- Resultado: Passou  
---

## 🔹 3. Reflexão

### Foi difícil escrever testes antes do código?
Sim, pensar nas regras de negócio e em outros detalhes antes de escrever o código é muito mais complexo do que apenas escrever o código e testar e/ou validar depois

---

### O TDD ajudou no desenvolvimento?
Mais ou menos, TDD, apesar de auxiliar na organização do desenvolvimento, tem uma curva de aprendizado e adaptação um pouco íngrime, o que faz com que leve um tempo considerável para se adaptar ao método, desaclerando os processos. Além de haver estapas que podem ser consideradas suboptimas quando o assunto é desenvolvimento. A "necessidade" de falhar nos testes mesmo sabendo o que está errado é limitante

---

### Os testes aumentaram a confiança no código?
Sim, os testes permitiram que o código pudesse ser refatorado e auterado sem medo de que tudo parasse de funcionar

---

### O que melhorariam?
- Mais cenários extremos
- Cobertura maior  
- Pular algumas etapas do TDD para aumentar a velocidade
---

### Como isso ajuda no projeto?
Assegura que a equipe consiga sempre aumentar a qualidade do projeto sem risco de cometer falhas críticas que afetem seu funcionamento
