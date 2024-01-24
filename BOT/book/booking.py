import book.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Booking(webdriver.Chrome):
    def __init__(self,teardown=False):
        self.teardown = teardown
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        super(Booking,self).__init__(options=chr_options)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)