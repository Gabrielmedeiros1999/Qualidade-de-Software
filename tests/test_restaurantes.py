from pages.restaurantes_page import RestaurantesPage

def test_visualizar_restaurantes(page):
    restaurantes = RestaurantesPage(page)

    restaurantes.acessar()
    restaurantes.visualizar_restaurantes()

    assert page.locator("body").is_visible()