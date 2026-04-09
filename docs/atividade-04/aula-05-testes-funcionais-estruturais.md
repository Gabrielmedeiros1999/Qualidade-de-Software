# 🧪 Aula 5 – Testes Funcionais vs Estruturais  
## LocalEats

---

## 👥 Integrantes do Grupo
- Gabriel Caldeira Medeiros
- Vinicius Dobke
 
---

## 🎯 1. Funcionalidade escolhida

**Funcionalidade selecionada:**  
Busca de restaurantes

**Descrição da funcionalidade:**  
A funcionalidade de busca de restaurantes permite que o usuário pesquise estabelecimentos com base em nome, tipo de comida ou localização. O sistema retorna uma lista de restaurantes que correspondem aos critérios informados.

**O que o usuário espera:**  
O usuário espera encontrar resultados corretos, relevantes e rápidos. Além disso, espera que a busca funcione mesmo com pequenas variações e que não retorne resultados incorretos ou vazios sem motivo.

---

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)

**Quais testes vocês fariam sem conhecer o código?**

### 🔹 Cenários de teste

- Cenário 1:  
  Buscar por um nome de restaurante existente -> Deve retornar o restaurante correto

- Cenário 2:  
  Buscar por tipo de comida, exemplo pizza -> Deve retornar restaurantes relacionados

- Cenário 3:
  Buscar por tipo de culinária, exemplo chinesa -> Deve retornar restaurantes relacionados
  
- Cenário 4:  
  Buscar por um nome de restaurante inexistente -> Deve retornar que o nome não foi encontrado e mostrar restaurantes com nomes semelhantes à busca em forma de sugestão

---

### 🔹 Possíveis erros identificados

-  Não retornar resultados mesmo existindo restaurantes
-  Retornar restaurantes que não têm relação com a busca
-  Retornar apenas alguns restaurantes que tem relação com a busca
-  Retornar resultados repetidos

---

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)

**Como essa funcionalidade poderia estar implementada internamente?**

### 🔹 Lógica hipotética (pseudo-código ou descrição)

```pseudo
Recebe entrada de texto do usuário e/ou filtros que o usuário escolher
Verifica se há algum restaurante correspondente aos parâmetros que o usuário inseriu
Se houver, retorna ao usuário todos os restaurantes correspondertes
Se não houver, notifica o usuário que não há restaurante que atende os parâmetros
Caso seja uma busca por nome, retorna ao usuário restaurantes com nome semelhante ao que o usuário inseriu

```

### 🔹 Situações a serem testadas

- Situação 1: Se forem inseridos parâmetros válidos e houverem resultados possíveis, eles são retornados
- Situação 2: Se forem inseridos parâmetros válidos e não houverem resultados possíveis, o sistema notifica o usuário
- Situação 3: Se forem inseridos parâmetros inválidos, o sistema notifica o usuário e não realiza busca

### 🔹 Possíveis erros identificados

- Com parâmetros inválidos, o sistema realiza a busca e retorna um vazio
- Com parâmetros válidos, o sistema ignora os filtros do usuário
- Com parâmetros válidos, o sistema devolve erro de parâmetros inválidos

## ⚖️ 4. Comparação entre as abordagens

#Qual a principal diferença entre testar sem ver o código e com acesso ao código?

Testar sem ver o código foca no comportamento do sistema do ponto de vista do usuário. Já testar com acesso ao código analisa a lógica interna, verificando como o sistema foi implementado.

Que tipo de problema cada abordagem ajuda a encontrar?

Caixa-preta:
<!-- Problemas de lógica, conformidade com requisitos e outros problemas relacionados com o planejamento do produto-->
Caixa-branca:
<!-- Erros de código, sintaxe e outros problemas referentes ao código propriamente dito -->

## 💡 5. Reflexão no contexto do LocalEats

Qual abordagem parece mais importante neste momento do projeto?

<!-- Considerando os problemas encontrados, os mais importantes nesse momentos são os testes de caixa branca -->

Apenas uma abordagem seria suficiente? Por quê?

<!-- Neste caso sim, pois e equipe já aparenta ter seus requisitos e funcionalidades definidos na etapa de planejamento, o que necessita de ser feito é consertar o comportamento das funcionalidades e corrigir falhas em código -->

## 🚀 Conclusão

A equipe aprendeu a diferença entre testes funcionais e testes estruturais além da importância de ambos para um projeto e como eles fazem a diferença para o planejamento e desenvolvimento de um produto com qualidade
