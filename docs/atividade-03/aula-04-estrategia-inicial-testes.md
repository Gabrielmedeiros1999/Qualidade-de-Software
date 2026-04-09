# Estratégia Inicial de Testes – LocalEats

**Disciplina:** Qualidade de Software  
**Equipe:** fila1  
**Integrantes:** Gabriel Caldeira Medeiros, Vinicius Dobke  

---

## 1. Funcionalidades principais

- Login
- Avaliações de usuários
- Salvar favoritos
- Busca de restaurantes
- Recomendações personalizadas
- Compartilhar experiências

---

## 2. Níveis de teste

### Funcionalidade: Login
- Unitário: validar senha e campos obrigatórios
- Integração: verificar conexão entre front-end e API
- Sistema: usuário faz login completo
- Aceitação: usuário entra no sistema sem erro

### Funcionalidade: Avaliações de Usuários
- Unitário: validar número de estrelas e campo de texto
- Integração: verificar conexão entre front-end e API
- Sistema: usuario publica avaliação
- Aceitação: usuario avalia restaurante sem erro

### Funcionalidade: Salvar Favoritos
- Unitário: validar botão de salvar nos favoritos
- Integração: verificar conexão entre front-end e API
- Sistema: usuario salva nos favoritos
- Aceitação: usuario adiciona restaurante aos favoritos sem erro

### Funcionalidade: Busca de Restaurantes
- Unitário: Validação da lógica de filtros 
- Integração: verificar conexão entre front-end, API e banco de dados na busca 
- Sistema: Usuário realiza busca completa e recebe resultados 
- Aceitação: Usuário consegue encontrar restaurantes relevantes corretamente

### Funcionalidade: Recomendações personalizadas
- Unitário: validação da lógica de recomendações
- Integração: verificar conexão entre front-end, API e banco de dados
- Sistema: Usuario recebe recomendações únicas para seu perfil
- Aceitação: Sistema identifica e envia recomendações ao usuario corretamente

### Funcionalidade: Compartilhar experiências
- Unitário: validação de campos obrigatórios
- Integração: verificar conexão entre front-end e banco de dados
- Sistema: usuario publica sua experiência
- Aceitação: usuario tem sua experiência publicada sem erro

---

## 3. Prioridades e riscos

#Alta prioridade:
- Login → sem login o usuário não usa o sistema
- Busca de restaurantes → principal funcionalidade do sistema

Justificativa:
Falhas nessas áreas impedem o uso da plataforma.

#Baixa prioridade:
- Avaliações de usuários → importante para usuários identificarem melhores restaurantes
- Recomendações personalizadas → A ausência pode fazer parecer que a plataforma é inferior à concorrentes
- Favoritos → não impede o uso, serve apenas para marcar restaurantes que mais gosta
- Compartilhar experiências → não impede o uso, é apenas uma funcionalidade de interação com comunidade

Justificativa:
Funcionalidades não essenciais para uso mas que aumentam a satisfação do usuário

---

## 4. Pirâmide de Testes

- Maior foco: Testes unitários
- Médio foco: Testes de integração e sistema
- Menor foco: Testes de Aceitação

Justificativa:
Testes unitários são os mais baratos, rápidos e fáceis, devem ter o maior foco possível para garantir uma base solida. Testes de integração e sistema tem um custo um pouco maior, mas ainda são bastante importantes para que o sistema funcione da maneira devida e conforme as regras de negócio. Testes de aceitação tem um custo elevado e tendem a possuir uma complexidade maior, o que os torna menor prioridade nesse contexto, especialmente considerando que há uma base bastante confiável de testes.

---

## 5. Testes em Produção

- O sistema usará testes em produção de forma reduzida e cautelosa, para evitar problemas maiores
- Os testes em produção serão utilizados única e exclusivamente para novas funcionalidades de complexidade elevada a serem lançadas futuramente

Justificativa:
Essa abordagem visa diminuir o custo necessário para testes, além de evitar ao máximo possíveis falhas e outros problemas que podem vir a ser causados por testes em produção. Juntamente disso, essa abordagem também permite que a equipe de DevOps possa focar seus esforços em papeis mais importantes.
