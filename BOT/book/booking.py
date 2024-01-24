import book.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Booking(webdriver.Chrome):
    def __init__(self,teardown=False):
        self.teardown = teardown
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        super(Booking,self).__init__(options=chr_options)
        self.maximize_window()
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)


