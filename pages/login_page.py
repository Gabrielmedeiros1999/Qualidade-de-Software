class LoginPage:
    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto("https://local-eats-unisenac.vercel.app/static/login.html")

    def realizar_login(self, email, senha):
        self.page.get_by_role("textbox", name="teste@teste.com").fill(email)
        self.page.locator('#loginPassword').fill(senha)
        self.page.locator("#loginForm button").click()