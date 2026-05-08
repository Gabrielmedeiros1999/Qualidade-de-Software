from pages.login_page import LoginPage

def test_login_com_sucesso(page):
    login = LoginPage(page)

    login.acessar()
    login.realizar_login("novo23@teste.com", "gbd34")

    assert page.locator("body").is_visible()