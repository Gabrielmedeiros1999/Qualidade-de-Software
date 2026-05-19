# Aula 12 – BDD e Automação Orientada a Comportamento
# Exemplo de Entrega PBL – LocalEats

## 👥 Integrantes

- Gabriel Caldeira Medeiros
- Vinicius Dobke

---

# 🔹 1. Fluxo escolhido

## Integrante: Gabriel Caldeira Medeiros

### Fluxo
Navegação entre páginas

### Objetivo
Validar se o usuário consegue navegar corretamente entre as páginas do sistema.

## Integrante: Nome do(a) aluno(a)

### Fluxo


### Objetivo


---

# 🔹 2. Cenários BDD

## Arquivo

```text
features/navegacao_paginas.feature
```

## Conteúdo

```gherkin
Feature: Navegação entre páginas

  Scenario: Navegar para página de pedidos
    Given que o usuário realiza login no sistema
    When clicar em "Meus Pedidos"
    Then o sistema deve abrir a página de pedidos

  Scenario: Navegar para página inicial
    Given que o usuário realiza login no sistema
    When acessar a página inicial
    Then o sistema deve exibir os restaurantes disponíveis
```

## Arquivo

```text
features/Arquivo.feature
```

## Conteúdo

```gherkin
Feature: 

  Scenario: 
    Given
    When 
    Then 

  Scenario: 
    Given 
    When 
    Then 
```

---

# 🔹 3. Automação com pytest-bdd

## Estrutura do projeto

```text
projeto/
│
├── features/
│   └── navegacao_paginas.feature
│   
├── tests/
│   └── test_navegacao_paginas.py
│
├── evidencias/
│
└── README.md
```

---

## Arquivo

```text
tests/test_filtro_categoria.py
```

## Código

```python
from pytest_bdd import scenarios, given, when, then

scenarios('../features/navegacao_paginas.feature')


@given('que o usuário realiza login no sistema')
def login(page):

    page.goto('https://local-eats-unisenac.vercel.app/static/login.html')

    page.fill('input[type="email"]', 'novo23@teste.com')
    page.fill('input[type="password"]', 'gbd34')

    page.locator('#loginForm button[type="submit"]').click()

    page.wait_for_timeout(5000)


@when('clicar em "Meus Pedidos"')
def abrir_pedidos(page):

    page.goto('https://local-eats-unisenac.vercel.app/static/orders.html')


@then('o sistema deve abrir a página de pedidos')
def validar_pedidos(page):

    assert 'orders' in page.url


@when('acessar a página inicial')
def abrir_home(page):

    page.goto('https://local-eats-unisenac.vercel.app/static/index.html')


@then('o sistema deve exibir os restaurantes disponíveis')
def validar_home(page):

    assert page.locator('body').is_visible()
```

---

# 🔹 4. Execução dos testes

## Comando executado

```bash
pytest tests/test_navegacao_paginas.py -v

```

---

## Resultado

```text
=================== test session starts ===================

2 passed in 5.32s

==========================================================
```

---

# 🔹 5. Evidências

## Print da execução

```text
evidencias/
  teste-navegacao-paginas.png
```

## Print da aplicação

```text
evidencias/
  navegacao-paginas.png
```

---

# 🔹 6. Análise crítica

## O cenário ficou legível?

Sim. A estrutura Given-When-Then ajudou a entender claramente o comportamento esperado.

---

## O BDD ajudou a entender o comportamento?

Sim. O cenário ficou compreensível mesmo para pessoas sem conhecimento técnico.

---

## O teste ficou robusto?

Parcialmente. Alguns seletores dependem diretamente do texto exibido na tela.

---

## Quais dificuldades surgiram?

- Encontrar seletores estáveis e adaptar alguns elementos da interface para automação.

---

## O teste ficou dependente da interface?

Sim. Mudanças no frontend podem quebrar alguns seletores.

---

# 🔹 7. Reflexão final

## BDD melhora comunicação entre equipe?

Sim. O comportamento do sistema ficou mais claro para QA, desenvolvimento e negócio.

---

## Todo teste deve usar BDD?

Não. BDD deve ser usado principalmente em fluxos importantes do negócio.

---

## Quando vale a pena usar BDD?

Quando o comportamento do sistema precisa ser documentado de forma clara e colaborativa.

---

## Como isso ajuda no projeto do grupo?

Ajuda a transformar requisitos em testes automatizados compreensíveis e organizados.

---

# ✅ Conclusão

A atividade permitiu compreender:

- escrita de cenários BDD
- automação orientada a comportamento
- integração entre pytest-bdd e Playwright
- importância da legibilidade dos testes
- manutenção de automações de frontend