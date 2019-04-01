from selenium import webdriver
import unittest
import HtmlTestRunner

from selenium.webdriver import ActionChains   #for hover on menue
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep



class RovsingMenu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='..\drivers\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get('http://rovsing.dk/')

    def test_company_menu(self):
        #self.driver.get('http://rovsing.dk/')
        companyMenu1 = "//li[@id='menu-item-3361']"
        aboutUs = "//li[@id = 'menu-item-3004']"
        contactUs = "//li[@id = 'menu-item-3132']"
        management = "//li[@id = 'menu-item-3008']"

        self.driver.find_element_by_class_name('easy-cookies-policy-accept').click()
        self.driver.implicitly_wait(10)

        companyMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3361']")
        management_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3008']")
        contact_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3132']")
        action = ActionChains(self.driver)
        # self.driver.save_screenshot("homepag.png")
        # action.move_to_element(companyMenu).move_to_element(contact_subMenu).click().perform()
        # cmn = WebDriverWait(self.driver, 10).until(lambda driver: companyMenu)
        action.move_to_element(companyMenu).move_to_element(contact_subMenu).click().perform()

        # filling contact form

        name_textbox = "//input[ @ placeholder = '*Name']"
        compnay_textbox = "//input[@id='company']"
        title_textbox = "//input[@id='title']"
        email_textbox = "//input[@id='email']"
        country_textbox = "//input[@id='country']"
        phone_textbox = "//input[@id='phone']"
        sale_textbox = "//select[@id='sales']"
        message_textbox = "//textarea[@id='message']"
        submit_btn = "//input[@id='send-btn']"

        # self.driver.find_element_by_xpath(name_textbox).send_keys("Mumtaz Maqsood")
        self.driver.find_element_by_xpath(compnay_textbox).send_keys("abc compnay")
        self.driver.find_element_by_xpath(title_textbox).send_keys("need info")
        self.driver.find_element_by_xpath(email_textbox).send_keys("mm@gmail.com")
        self.driver.find_element_by_xpath(country_textbox).send_keys("Denmark")
        self.driver.find_element_by_xpath(phone_textbox).send_keys("12345670")
        self.driver.find_element_by_xpath(sale_textbox).send_keys("Business and development")
        self.driver.find_element_by_xpath(message_textbox).send_keys("here is message")
        self.driver.find_element_by_xpath(submit_btn).click()
        sleep(5)

    def test_solution_menu(self):
        solutionMenu = self.driver.find_element_by_xpath("//ul[@id='menu-main-navigation']/li[2]")
        solutionMenu_productMenu = self.driver.find_element_by_xpath("//li[@id = 'menu-item-2932']")
        solutionMenu_productMenu_2 = self.driver.find_element_by_xpath("//li[@id = 'menu-item-3335']")

        action = ActionChains(self.driver)
        action.move_to_element(solutionMenu).move_to_element(solutionMenu_productMenu).perform()
        self.driver.implicitly_wait(20)
        solutionMenu_productMenu_2.click()
        self.driver.implicitly_wait(10)
        #sleep(5)

    def test_news_menu(self):
        newsMenu_xpath = self.driver.find_element_by_xpath("//span[contains(text(),'News')]")
        newsMenu_xpath.click()
        sleep(5)

    def test_search_menu(self):
        searchMenu_xpath = self.driver.find_element_by_xpath("//a[@id='home1id']")
        search_box = self.driver.find_element_by_xpath("//div[@id='search_cls']")
        searchMenu_xpath.click()
        self.driver.implicitly_wait(30)
        search_box.send_keys("hello world")
        sleep(10)

    def test_career_menu(self):
        careerMenu_xpath = self.driver.find_element_by_xpath("//li[@id='menu-item-3225']")
        unsolicitedApp_xpath = self.driver.find_element_by_xpath("//li[@id='menu-item-3002']")
        action = ActionChains(self.driver)
        action.move_to_element(careerMenu_xpath).move_to_element(unsolicitedApp_xpath).click().perform()
        sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))
