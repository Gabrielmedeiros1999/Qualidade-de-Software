from pytest_bdd import scenarios, given, when, then

scenarios('../features/navegacao_paginas.feature')


@given('que o usuário realiza login no sistema')
def login(page):

    page.goto('https://local-eats-unisenac.vercel.app/static/login.html')

    page.fill('input[type="email"]', 'novo23@teste.com')
    page.fill('input[type="password"]', 'gbd34')

    page.locator('#loginForm button[type="submit"]').click()

    page.wait_for_timeout(5000)


@when('clicar em "Meus Pedidos"')
def abrir_pedidos(page):

    page.goto('https://local-eats-unisenac.vercel.app/static/orders.html')


@then('o sistema deve abrir a página de pedidos')
def validar_pedidos(page):

    assert 'orders' in page.url


@when('acessar a página inicial')
def abrir_home(page):

    page.goto('https://local-eats-unisenac.vercel.app/static/index.html')


@then('o sistema deve exibir os restaurantes disponíveis')
def validar_home(page):

    assert page.locator('body').is_visible()