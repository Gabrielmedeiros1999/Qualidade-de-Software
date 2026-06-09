# Aula 15 – Modelos de Maturidade

## Integrantes

- Gabriel Caldeira Medeiros
- Vinicius Dobke

---

# 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
|-----------|-----|----------|-----|
| Os requisitos são documentados? | | X | |
| Existe controle de mudanças? | | | X |
| Há atividades de teste definidas? | | X | |
| Os defeitos são registrados? | X | | |
| O processo de desenvolvimento é conhecido por toda a equipe? | X | | |
| As tarefas são planejadas e acompanhadas regularmente? | | X | |
| Existe padronização para implementação de funcionalidades? | | X | |
| Os testes são executados antes da entrega das funcionalidades? | X | | |
| Há revisão de código ou validação por outro integrante da equipe? | X | | |
| A equipe utiliza ferramentas para gerenciamento das atividades? | X | | |
| Os artefatos do projeto são organizados e versionados? | X | | |
| Existe rastreabilidade entre requisitos e funcionalidades? | | X | |
| A equipe realiza retrospectivas ou reuniões de melhoria? | | X | |
| Existem métricas para acompanhar a qualidade? | | | | X |

### Nível de maturidade estimado

**Gerenciado (CMMI Nível 2 / MPS.BR G)**

### Justificativa

A equipe possui um processo básico de desenvolvimento, com planejamento das tarefas, utilização de controle de versão através do GitHub e acompanhamento das funcionalidades implementadas. Os requisitos são registrados, embora nem sempre de forma detalhada, e existem atividades de teste antes das entregas. Dessa forma, o projeto apresenta características de um processo gerenciado.

---

# 2. Lacunas Identificadas

| Lacuna | Impacto |
|---------|----------|
| Ausência de métricas de qualidade | Dificulta medir a evolução do projeto e identificar problemas recorrentes |
| Registro informal de defeitos | Pode causar repetição de erros e dificultar correções futuras |
| Revisão de código não padronizada | Aumenta o risco de falhas passarem para produção |
| Rastreabilidade parcial entre requisitos e funcionalidades | Dificulta o controle de mudanças e manutenção |

---

# 3. Propostas de Melhoria

| Melhoria | Benefício |
|-----------|-----------|
| Definir métricas básicas (bugs encontrados, funcionalidades concluídas, cobertura de testes) | Melhor acompanhamento da qualidade |
| Criar um processo formal de revisão de código (Pull Requests) | Redução de defeitos e melhoria da padronização |
| Registrar defeitos e correções em ferramenta de acompanhamento | Maior controle e histórico de problemas |
| Melhorar a documentação dos requisitos | Facilita manutenção e desenvolvimento futuro |
| Realizar retrospectivas ao final de cada entrega | Promove melhoria contínua do processo |

---

## Conclusão

O processo atual da equipe demonstra características de um nível gerenciado de maturidade, pois existe planejamento, controle das atividades e utilização de ferramentas de versionamento. No entanto, ainda há oportunidades de evolução relacionadas à padronização dos processos, uso de métricas e melhoria do controle de qualidade. Com a adoção das melhorias propostas, a equipe poderá evoluir para níveis mais elevados de maturidade, tornando o desenvolvimento mais previsível, eficiente e confiável.