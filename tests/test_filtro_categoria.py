from pytest_bdd import scenarios, given, when, then

scenarios('../features/filtro_categoria.feature')


@given('que o usuário está logado no sistema')
def login(page):

    page.goto('https://local-eats-unisenac.vercel.app/static/login.html')

    page.fill('input[type="email"]', 'novo23@teste.com')
    page.fill('input[type="password"]', 'gbd34')

    page.locator('#loginForm button[type="submit"]').click()

    page.wait_for_timeout(5000)

    page.goto('https://local-eats-unisenac.vercel.app/static/index.html')

    page.wait_for_timeout(3000)

    page.pause()

@when('selecionar a categoria "Japonesa"')
def selecionar_japonesa(page):

    page.locator('[data-cuisine="Japonesa"]').click()


@then('o sistema deve manter a página de exploração ativa')
def validar_japonesa(page):

    assert "index" in page.url


@when('selecionar a categoria "Brasileira"')
def selecionar_brasileira(page):

    page.locator('[data-cuisine="Brasileira"]').click()


@then('o sistema deve atualizar a listagem de restaurantes')
def validar_brasileira(page):

    assert page.locator("body").is_visible()