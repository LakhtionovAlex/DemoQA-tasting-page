class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    # открывает базовую страницу
    def visit(self):
        return self.driver.get(self.base_url)

    # возращает коректный url
    def get_url(self):
        return self.driver.current_url

    # возращает тру если страница верна
    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False
