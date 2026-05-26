# 🧩 Atividade PBL – Aula 10  
## Testes Funcionais Automatizados – LocalEats

---

## 👥 Integrante(s)
- Gabriel Caldeira Medeiros 
- Vinicius Dobke  

---

## 🔹 1. Fluxo funcional escolhido

### 📌 Gabriel Medeiros — Login de usuário:
Login de usuário

🔎 **Descrição**  
Permite autenticar um usuário no sistema.

🎯 **Importância**  
Fluxo essencial para acesso às funcionalidades do LocalEats.

📏 **Cenários esperados**
- Login válido → sucesso
- Login inválido → mensagem de erro
- Campos vazios → validação

### 📌 Vinicius Dobke —  Fluxo Escolhido:
Navegação e visualização de restaurantes

🔎 **Descrição**  
Permite ao usuário visualizar a lista de restaurantes disponíveis no sistema.

🎯 **Importância**  
É uma funcionalidade essencial para que o usuário possa conhecer os restaurantes antes de realizar um pedido.

📏 **Cenários esperados**
- Lista carregada corretamente
- Restaurantes visíveis na tela
- Navegação funcionando sem erros

---

## 🔹 2. Teste com Codegen

### 💻 Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### 🔗 Gabriel Medeiros - Link para o código gerado

👉 https://github.com/Gabrielmedeiros1999/Qualidade-de-Software/blob/main/tests/codegen_login.py

### 🔗 Vinicius Dobke - Link para o código gerado

👉 https://github.com/Gabrielmedeiros1999/Qualidade-de-Software/blob/main/tests/codegen_restaurantes.py

### 🧠 Observações

- O Codegen ajudou a iniciar rapidamente o teste  
- O código gerado é verboso  
- Foi necessário refatorar  

---

## 🔹 3. Teste automatizado com Pytest

### 🔗 Gabriel Medeiros - Link para o teste

👉 https://github.com/Gabrielmedeiros1999/Qualidade-de-Software/blob/main/tests/test_login.py

### 📌 O que o teste faz?

- Acessa o sistema  
- Realiza login  
- Valida execução do fluxo de login

### 🔗 Vinicius Dobke - Link para o teste

👉 https://github.com/Gabrielmedeiros1999/Qualidade-de-Software/blob/main/tests/test_restaurantes.py

### 📌 O que o teste faz?
- Acessa o sistema
- Verifica se a lista de restaurantes é carregada
- Seleciona um restaurante
- Valida a abertura da página de detalhes
---

## 🔹 4. Refatoração com Page Object Model (POM)

### 🔗 Gabriel Medeiros - Link para Page Object

👉 https://github.com/Gabrielmedeiros1999/Qualidade-de-Software/blob/main/pages/login_page.py

### 🔗 Gabriel Medeiros - Link para teste refatorado

👉 https://github.com/Gabrielmedeiros1999/Qualidade-de-Software/blob/main/tests/test_login.py

### 🧠 Melhorias realizadas

- Separação entre teste e lógica de UI  
- Código mais organizado  
- Maior reutilização

### 🔗 Vinicius Dobke - Link para Page Object

👉 https://github.com/Gabrielmedeiros1999/Qualidade-de-Software/blob/main/pages/restaurantes_page.py

### 🔗 Vinicius Dobke - Link para teste refatorado

👉 https://github.com/Gabrielmedeiros1999/Qualidade-de-Software/blob/main/tests/test_restaurantes.py

### 🧠 Melhorias realizadas

- Separação da lógica de navegação da lógica de teste
- Reutilização de métodos para acesso aos restaurantes
- Melhor legibilidade e manutenção do código
- Redução da dependência de seletores frágeis

---

## 🔹 5. Execução dos testes

### ▶️ Comando

```bash
pytest

python -m pytest tests/test_login.py -v

python -m pytest tests/test_restaurantes.py -v
```

### 📊 Resultado

- Total de testes: 2
- Testes passaram: 2  
- Testes falharam: 0  

### 📸 Evidência

![Execução dos testes](https://raw.githubusercontent.com/Gabrielmedeiros1999/Qualidade-de-Software/main/evidencias/teste-playwright.png)

![Execução do teste restaurante](https://raw.githubusercontent.com/Gabrielmedeiros1999/Qualidade-de-Software/main/evidencias/teste-playwright-restaurantes.png)

---

## 🔹 6. Análise crítica

- O teste apresentou falhas durante o desenvolvimento devido à fragilidade dos seletores gerados automaticamente pelo Codegen.
- Seletores baseados em texto e placeholders podem quebrar facilmente após mudanças no frontend.
- Foi necessário refatorar os locators utilizando IDs específicos para tornar o teste mais confiável.

---

## 🔹 7. Reflexão

- Testes automatizados não substituem testes manuais, mas reduzem tarefas repetitivas.  
- Devem focar em fluxos críticos  
- Fluxos como login, carrinho e checkout devem receber maior prioridade. 
- A automação aumenta a confiança em alterações no sistema e reduz falhas em deploys.
- O uso do Playwright facilitou a automação E2E e aproximou os testes da experiência real do usuário.

---

## 💡 Conclusão

A automação de testes melhora a qualidade, mas exige boas práticas para manutenção.
