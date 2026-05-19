Feature: Navegação entre páginas

  Scenario: Navegar para página de pedidos
    Given que o usuário realiza login no sistema
    When clicar em "Meus Pedidos"
    Then o sistema deve abrir a página de pedidos

  Scenario: Navegar para página inicial
    Given que o usuário realiza login no sistema
    When acessar a página inicial
    Then o sistema deve exibir os restaurantes disponíveis