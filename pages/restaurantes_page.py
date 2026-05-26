class RestaurantesPage:
    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto("https://local-eats-unisenac.vercel.app/")

    def visualizar_restaurantes(self):
        self.page.wait_for_load_state("networkidle")