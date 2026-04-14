# Aula 6 – Planejamento e Execução de Testes

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrantes do grupo:  
> - Gabriel Caldeira Medeiros 
> - Vinicius Dobke

---

# 1. Plano de Testes

## 1.1 Objetivo
Descreva o objetivo do plano de testes.

> Validar as principais funcionalidades do sistema LocalEats, garantindo que o usuário consiga navegar, buscar restaurantes, realizar pedidos e avaliar serviços de forma correta, sem erros ou comportamentos inesperados.

---

## 1.2 Escopo

### O que será testado
- Login e cadastro de usuários
- Busca de restaurantes
- Realização de pedidos

### O que NÃO será testado
- Desempenho em larga escala
- Testes de segurança avançados

---

## 1.3 Funcionalidades selecionadas
Liste as funcionalidades que serão foco dos testes:

- Login/Cadastro
- Busca de restaurantes
- Pedido
- Avaliação
---

## 1.4 Estratégia de Testes

Descreva como os testes serão realizados.

- Tipos de teste:
  - (X) Funcional
  - (X) Usabilidade
  - ( ) Outros: _______

- Abordagem:
  > Testes manuais baseados em cenários previamente definidos, simulando o comportamento real do usuário na aplicação.

---

## 1.5 Responsáveis

Defina os papéis na equipe:

| Nome | Responsabilidade |
|------|----------------|
| Vinicius Dobke | Criação dos casos de teste |
| Gabriel Medeiros | Execução dos testes |

---

# 2. Casos de Teste

Crie no mínimo 5 casos de teste.

---

## CT-01 – Login com sucesso

**Pré-condição:**  

Usuário já cadastrado no sistema

**Passos:**  
1. Acessar a página de login 
2. Inserir email e senha válidos  
3. Clicar em "Entrar" 

**Dados de entrada (se aplicável):**  

Email: novo23@teste.com

Senha: gbd34

**Resultado esperado:**  
Usuário é redirecionado para a página inicial logado no sistema

---

## CT-02 – Login com senha incorreta

**Pré-condição:**  

Usuário já cadastrado

**Passos:**  
1. Acessar a página de login  
2. Inserir email válido e senha incorreta 
3. Clicar em "Entrar" 

**Dados de entrada (se aplicável):**  

Senha: errada123

**Resultado esperado:**  

Sistema exibe mensagem de erro e não permite login

---

## CT-03 – Buscar restaurante

**Pré-condição:**  

Usuário na página inicial

**Passos:**  
1.  Digitar nome de restaurante na busca
2.  Clicar em pesquisar

**Dados de entrada (se aplicável):**  

"Japonesa"

**Resultado esperado:**  

Lista de restaurantes relacionados aparece na tela

---

## CT-04 – Realizar pedido com sucesso

**Pré-condição:**  

Usuário logado

**Passos:**  
1. Selecionar um restaurante  
2. Escolher um item 
3. Clicar em "Pedir" 

**Dados de entrada (se aplicável):**  

Item: Prato Especial 0

**Resultado esperado:**  

Pedido é registrado com sucesso

---

## CT-05 – Avaliar restaurante

**Pré-condição:**  

Usuário logado

**Passos:**  
1. Acessar página de um restaurante
2. Tentar avaliar  

**Dados de entrada (se aplicável):**  

 Clicar nas Estrelas


**Resultado esperado:**  

Avaliação é registrada com sucesso

---

# 3. Execução dos Testes

Preencha a tabela com os resultados obtidos.

| ID     | Resultado (Passou/Falhou) | Evidência (descrição ou print) |
|--------|--------------------------|--------------------------------|
| CT-01  |    Passou                      |   Login realizado com sucesso                             |
| CT-02  |    Passou                      |   Mensagem de erro exibida (Invalid credentials)                             |
| CT-03  |    Falhou                      |   Resultados não são listados                             |
| CT-04  |    Passou                      |    Pedido foi registrado                            |
| CT-05  |    Falhou                      |     Não é possivel avaliar                           |

---

# 4. Análise dos Resultados

- Quantidade de testes executados:  5
- Quantidade de testes que passaram:  3
- Quantidade de testes que falharam:  2

## Principais problemas encontrados
- Falha na busca por culinária ou localização
- Não é possivel avaliar os restaurantes
- Entrando na pagina do restaurante favoritado, o butão de favorito fica desmarcado

---

# 5. Reflexão

Responda às questões abaixo:

- O plano de testes ajudou a organizar melhor o processo? Por quê?

  Sim, pois permitiu definir claramente o que deveria ser testado e como executar os testes.

- Algum problema só foi identificado durante a execução? Explique.

  Sim, o erro ao realizar busca só foi percebido durante a execução prática dos testes.

- O que o grupo melhoraria no processo de testes?

  Adicionar mais cenários de erro e testes automatizados para aumentar a cobertura.

---

## Conclusão

O sistema apresentou comportamento parcialmente aceitável, pois a maioria das funcionalidades funcionou corretamente, porém falhas críticas como erro na busca e não poder avaliar restaurante precisam ser corrigidas.

---

# 6. Conclusão Geral

Resumo final:

- Qualidade geral do sistema testado: Média
- Principais pontos positivos: Interface simples e pedido funcional
- Principais problemas identificados: Falha na busca 
- Impressão geral do grupo sobre o processo de testes: O sistema está funcional, mas precisa de ajustes para ser confiável
