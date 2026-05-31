Feature: Filtro por categoria

  Scenario: Filtrar restaurantes pela categoria Japonesa
    Given que o usuário está logado no sistema
    When selecionar a categoria "Japonesa"
    Then o sistema deve manter a página de exploração ativa

  Scenario: Filtrar restaurantes pela categoria Brasileira
    Given que o usuário está logado no sistema
    When selecionar a categoria "Brasileira"
    Then o sistema deve atualizar a listagem de restaurantes