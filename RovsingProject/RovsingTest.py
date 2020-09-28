from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains   #for hover on menue
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pytest


class RovsingMenu(unittest.TestCase):

    # code in setUpClass run once before test cases run
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get('http://rovsing.dk/')
        cls.driver.find_element_by_class_name('easy-cookies-policy-accept').click()

    # code in setUp runs before every test case
    @classmethod
    def setUp(self):

    # --------------------------------------------------------------------------------------
    # get XPath of "Company main menu" and move cursor over Company menu
    # --------------------------------------------------------------------------------------
        self.companyMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3361']")
        self.action = ActionChains(self.driver)
        self.company_MainMenu = self.action.move_to_element(self.companyMenu)
    # --------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------
    # Get XPATH of "Solution main menu" and move cursor over Solution menu
    # --------------------------------------------------------------------------------------
        self.solutionMenu = self.driver.find_element_by_xpath("//ul[@id='menu-main-navigation']/li[2]")
        self.action_on_solutionMenu = ActionChains(self.driver)
        self.solution_mainMenu = self.action_on_solutionMenu.move_to_element(self.solutionMenu)
    # --------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------
    # Get XPATH of "Investor Relations main menu" and move cursor over Investor Relations menu
    # --------------------------------------------------------------------------------------
        self.investorRelations = self.driver.find_element_by_xpath("//li[@id='menu-item-3754']")
        self.action_on_investorRelation_Menu = ActionChains(self.driver)
        self.investorRelations_mainMenu = self.action_on_investorRelation_Menu.move_to_element(self.investorRelations)
    # --------------------------------------------------------------------------------------


    # --------------------------------------------------------------------------------------
    # Get XPATH of "Investor Relations main menu" and move cursor over Investor Relations menu
    # --------------------------------------------------------------------------------------
        self.careersXpath = self.driver.find_element_by_xpath("//li[@id='menu-item-3225']")
        self.action_on_careers_Menu = ActionChains(self.driver)
        self.careers_mainMenu = self.action_on_careers_Menu.move_to_element(self.careersXpath)
    # --------------------------------------------------------------------------------------





    # ---------------------------------------------------------------------------------
    # TEST CASES 1  > START : MAIN MENU -- Company --> Sub Menus
    #               (About us, Board of Directors, Management, customers, Contact Us)
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    #  START TEST CASE 1.1 : CLICK ON SUB_MENU "ABOUT US"
    # ---------------------------------------------------------------------------------
    def test_aboutUs_subMenu(self):
        aboutUs_subMenu = self.driver.find_element_by_xpath("//li[@id = 'menu-item-3004']")
        self.company_MainMenu.move_to_element(aboutUs_subMenu).click().perform()
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 1.1
    # ---------------------------------------------------------------------------------


    # ---------------------------------------------------------------------------------
    # START TEST CASE 1.2 : CLICK ON SUB_MENU "BOARD OF DIRECTORS"
    # ---------------------------------------------------------------------------------
    def test_boardOfDirectors_subMenu(self):

        boardofDirectors_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3005']")
        self.company_MainMenu.move_to_element(boardofDirectors_subMenu).click().perform()

    # --------------------------------------------------------------------------------------
    #  END TEST CASE 1.2
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 1.3 : CLICK ON SUB_MENU "CUSTOMERS"
    # ---------------------------------------------------------------------------------
    def test_Customers_subMenu(self):

        customers_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3007']")
        self.company_MainMenu.move_to_element(customers_subMenu).click().perform()

    # --------------------------------------------------------------------------------------
    #  END TEST CASE 1.3
    # ---------------------------------------------------------------------------------


    # ---------------------------------------------------------------------------------
    # START TEST CASE 1.4: CLICK ON SUB_MENU "MANAGEMENT"
    # ---------------------------------------------------------------------------------
    def test_management_subMenu(self):

        management_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3008']")
        self.company_MainMenu.move_to_element(management_subMenu).click().perform()

    # --------------------------------------------------------------------------------------
    #  END TEST CASE 1.4
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 1.5 : CLICK ON SUB_MENU "CONTACT US"
    # ---------------------------------------------------------------------------------

    def test_contactUs_subMenu(self):

        contact_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3132']")
        self.company_MainMenu.move_to_element(contact_subMenu).click().perform()

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

    # ---------------------------------------------------------------------------------
    #  END TEST CASE 1.5
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # END OF TEST CASES 1 : MAIN MENU -- Company --> Sub Menus
    #               (About us, Board of Directors, Management, customers, Contact Us)
    # ---------------------------------------------------------------------------------



    # ---------------------------------------------------------------------------------
    # TEST CASES 2  > START : MAIN MENU -- Solution --> Sub Menus
    #    (EGSE SYSTEMS, PRODUCTS, SOFTWARE, ON BOARD & GROUND SUPPORT,
    #    ON SITE ENGINEERING SUPPORT, SOFTWARE VERIFICATION AND VALIDATION)
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 2.1 : CLICK ON SUB_MENU "EGSE Systems"
    # ---------------------------------------------------------------------------------
    def test_egse_system_subMenu(self):
        egse_system_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-2931']")
        self.solution_mainMenu.move_to_element(egse_system_subMenu).click().perform()
        sleep(5)

    # ---------------------------------------------------------------------------------
    #  END TEST CASE 2.1
    # ---------------------------------------------------------------------------------

    #
    # ---------------------------------------------------------------------------------
    # START TEST CASE 2.2 : CURSOR MOVES ON SUB_MENU "Product" AND CLICK ON SUB_MENU
    # ---------------------------------------------------------------------------------
    def test_product_subMenu(self):
        # solutionMenu = self.driver.find_element_by_xpath("//ul[@id='menu-main-navigation']/li[2]")
        solutionMenu_productMenu = self.driver.find_element_by_xpath("//li[@id = 'menu-item-2932']")
        solutionMenu_productMenu_2 = self.driver.find_element_by_xpath("//li[@id = 'menu-item-3335']")

        # action = ActionChains(self.driver)
        # action.move_to_element(solutionMenu).move_to_element(solutionMenu_productMenu).perform()
        self.solution_mainMenu.move_to_element(solutionMenu_productMenu).perform()

        solutionMenu_productMenu_2.click()
        self.driver.implicitly_wait(10)
        #sleep(5)

    # ---------------------------------------------------------------------------------
    #  END TEST CASE 2.2
    # ---------------------------------------------------------------------------------



    # ---------------------------------------------------------------------------------
    # START TEST CASE 2.3 : CLICK ON SUB_MENU "SOFTWARE"
    # ---------------------------------------------------------------------------------
    def test_software_subMenu(self):
        software_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-2933']")
        self.solution_mainMenu.move_to_element(software_subMenu).click().perform()
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 2.3
    # ---------------------------------------------------------------------------------


    # ---------------------------------------------------------------------------------
    # START TEST CASE 2.4 : CLICK ON SUB_MENU "ON BOARD AND GROUND SUPPORT"
    # ---------------------------------------------------------------------------------
    def test_onGroundSupport_subMenu(self):
        onGroundSupport_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-2934']")
        self.solution_mainMenu.move_to_element(onGroundSupport_subMenu).click().perform()
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 2.4
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 2.5 : CLICK ON SUB_MENU "ON SITE ENGINEERING SUPPORT"
    # ---------------------------------------------------------------------------------
    def test_onSiteEngineeringSuppot_subMenu(self):
        onSiteEngineeringSuppot_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-2935']")
        self.solution_mainMenu.move_to_element(onSiteEngineeringSuppot_subMenu).click().perform()

    # ---------------------------------------------------------------------------------
    #  END TEST CASE 2.5
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 2.6 : CLICK ON SUB_MENU "SOFTWARE VERIFICATION AND VALIDATION"
    # ---------------------------------------------------------------------------------
    def test_swVerfication_subMenu(self):
        swVerfication_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-2936']")
        self.solution_mainMenu.move_to_element(swVerfication_subMenu).click().perform()
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 2.6
    # ---------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------
    # END TEST CASES 2  > START : MAIN MENU -- Solution --> Sub Menus
    #    (EGSE SYSTEMS, PRODUCTS, SOFTWARE, ON BOARD & GROUND SUPPORT,
    #    ON SITE ENGINEERING SUPPORT, SOFTWARE VERIFICATION AND VALIDATION)
    # ---------------------------------------------------------------------------------




    # ---------------------------------------------------------------------------------
    # TEST CASES 3  > START : MAIN MENU -- INVESTOR RELATIONS --> Sub Menus
    #    (ANNOUNCENMENTS, ANNUAL REPORT AND FINANCIAL INFORMATION, FINANCIAL CALENDER,
    #    CORPORATE GOVERENCE,INCENTIVE SCHEMES, ORDINERY GENERAL MEETINGS, CONVERTIBLE CREDIT FACLITY
    #    NASDAQ OMX)
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 3.1 : CLICK ON SUB_MENU "ANNOUNCEMENTS"
    # ---------------------------------------------------------------------------------
    def test_announments_subMenu(self):
        announments_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3648']")
        self.investorRelations_mainMenu.move_to_element(announments_subMenu).click().perform()
        sleep(2)

    # ---------------------------------------------------------------------------------
    #  END TEST CASE 3.1
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 3.2 : CLICK ON SUB_MENU "ANNUAL REPORT AND FINANCIAL INFORMATION"
    # ---------------------------------------------------------------------------------
    def test_annualReport_subMenu(self):
        annualReport_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-2994']")
        self.investorRelations_mainMenu.move_to_element(annualReport_subMenu).click().perform()
        sleep(2)
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 3.2
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 3.3 : CLICK ON SUB_MENU "FINANCIAL CALENDER"
    # ---------------------------------------------------------------------------------
    def test_financialCalender_subMenu(self):
        financialCalender_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-2996']")
        self.investorRelations_mainMenu.move_to_element(financialCalender_subMenu).click().perform()
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 3.3
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 3.4 : CLICK ON SUB_MENU "CORPORATE GOVERNANCE"
    # ---------------------------------------------------------------------------------
    def test_corporateGovernance_subMenu(self):
        corporateGovernance_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-2995']")
        self.investorRelations_mainMenu.move_to_element(corporateGovernance_subMenu).click().perform()
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 3.4
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 3.5 : CLICK ON SUB_MENU "INCENTIVE SCHEMES"
    # ---------------------------------------------------------------------------------
    def test_incentiveSchemes_subMenu(self):
        incentiveSchemes_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-2997']")
        self.investorRelations_mainMenu.move_to_element(incentiveSchemes_subMenu).click().perform()

    # ---------------------------------------------------------------------------------
    #  END TEST CASE 3.5
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 3.6 : CLICK ON SUB_MENU "ORDINARY GENERAL MEETINGS"
    # ---------------------------------------------------------------------------------
    def test_generalMeetings_subMenu(self):
        generalMeetings_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-2998']")
        self.investorRelations_mainMenu.move_to_element(generalMeetings_subMenu).click().perform()
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 3.6
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 3.7 : CLICK ON SUB_MENU "CONVERTIBLE CREDIT FACILITY"
    # ---------------------------------------------------------------------------------
    def test_creditFacility_subMenu(self):
        creditFacility_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-4179']")
        self.investorRelations_mainMenu.move_to_element(creditFacility_subMenu).click().perform()
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 3.7
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 3.8 : CLICK ON SUB_MENU "NASDAQ OMX "
    # ---------------------------------------------------------------------------------
    def test_nasdaq_subMenu(self):
        nasdaq_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3895']")
        self.investorRelations_mainMenu.move_to_element(nasdaq_subMenu).click().perform()
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 3.8
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # END TEST CASES 3  > MAIN MENU -- INVESTOR RELATIONS --> Sub Menus
    #    (ANNOUNCENMENTS, ANNUAL REPORT AND FINANCIAL INFORMATION, FINANCIAL CALENDER,
    #    CORPORATE GOVERENCE,INCENTIVE SCHEMES, ORDINERY GENERAL MEETINGS, CONVERTIBLE CREDIT FACLITY
    #    NASDAQ OMX)
    # ---------------------------------------------------------------------------------



    # ---------------------------------------------------------------------------------
    # TEST CASES 4  > START : MAIN MENU -- CAREERS --> Sub Menus
    #                       (OPEN POSITIONS, UNSOLICITED APPLICATION)
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 4.1 : CLICK ON SUB_MENU "OPEN POSITIONS"
    # ---------------------------------------------------------------------------------
    def test_openPositions_subMenu(self):
        openPositions_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3001']")
        self.careers_mainMenu.move_to_element(openPositions_subMenu).click().perform()

        # read more about the postion
        read_more = self.driver.find_element_by_xpath("//a[contains(text(),'Read more')]")
        read_more.click()

        # apply position
        apply_postion = self.driver.find_element_by_xpath("//div[@class='apply']")
        apply_postion.click()
        self.driver.implicitly_wait(5)

        # fill the form
        name_xpath = "//input[@id='name']"
        picture_xpath = "//input[@id='picturefile']"
        address_xpath = "//input[@id='address']"
        postal_xpath = "//input[@id='postalcode']"
        city_xpath = "//input[@id='city']"
        email_xpath = "//input[@id='your-email']"
        phone_xpath = "//div[7]//span[1]//input[1]"
        mobile_xpath = "//div[8]//span[1]//input[1]"
        jobTitle_xpath = "//input[@id='job-title']"
        experience_xpath = "//select[@id='exprience']"
        education_xpath = "//select[@id='exprience']"
        graduationYear_xpath = "//input[@id='yearofgraduation']"
        uploadCv_xpath = "//input[@id='uplaodcv']"
        term_xpath = "//input[@name='admited[]']"
        submitBtn_xpath = "//input[contains(@value,'Submit')]"

        # self.driver.switch_to_frame(0)

        # self.driver.find_element_by_xpath(name_xpath).send_keys("Mumtaz Maqsood")
        self.driver.find_element_by_xpath(picture_xpath).send_keys("C:/Users/mumtaz/Desktop/python/selenium/cv&pic/PIC.jpg")
        self.driver.find_element_by_xpath(address_xpath).send_keys("Høje Gladsaxe 33")
        self.driver.find_element_by_xpath(postal_xpath).send_keys("2860")
        self.driver.find_element_by_xpath(city_xpath).send_keys("Copenhagen")
        self.driver.find_element_by_xpath(email_xpath).send_keys("mumtaz.maqsood@yahoo.com")
        self.driver.find_element_by_xpath(phone_xpath).send_keys("71425482")
        self.driver.find_element_by_xpath(mobile_xpath).send_keys("00000")
        self.driver.find_element_by_xpath(jobTitle_xpath).send_keys("Tester")
        self.driver.find_element_by_xpath(experience_xpath).send_keys("2 years")
        self.driver.find_element_by_xpath(education_xpath).send_keys("M.Sc Computer & Information System")
        self.driver.find_element_by_xpath(graduationYear_xpath).send_keys("4")
        self.driver.find_element_by_xpath(uploadCv_xpath).send_keys("C:/Users/mumtaz/Desktop/python/selenium/cv&pic/sm cv+cl.pdf")
        self.driver.find_element_by_xpath(term_xpath).click()
        self.driver.find_element_by_xpath(submitBtn_xpath).click()
        sleep(5)
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 4.1
    # ---------------------------------------------------------------------------------


    # ---------------------------------------------------------------------------------
    # START TEST CASE 4.2 : CLICK ON SUB_MENU "UNSOLICITED APPLICATION"
    # ---------------------------------------------------------------------------------
    def test_unsolicitedApplication_subMenu(self):
        unsolicitedApplication_subMenu = self.driver.find_element_by_xpath("//li[@id='menu-item-3002']")
        self.action_on_careers_Menu.move_to_element(unsolicitedApplication_subMenu).click().perform()

        # fill the form
        name_xpath = "//input[@id='name']"
        picture_xpath = "//input[@id='picturefile']"
        address_xpath = "//input[@id='address']"
        postal_xpath = "//input[@id='postalcode']"
        city_xpath = "//input[@id='city']"
        email_xpath = "//input[@id='your-email']"
        phone_xpath = "//div[7]//span[1]//input[1]"
        mobile_xpath = "//div[8]//span[1]//input[1]"
        jobTitle_xpath = "//input[@id='job-title']"
        experience_xpath = "//select[@id='exprience']"
        education_xpath = "//select[@id='exprience']"
        graduationYear_xpath = "//input[@id='yearofgraduation']"
        uploadCv_xpath = "//input[@id='uplaodcv']"
        term_xpath = "//input[@name='admited[]']"
        submitBtn_xpath = "//input[contains(@value,'Submit')]"



        # self.driver.find_element_by_xpath(name_xpath).send_keys("Mumtaz Maqsood")
        self.driver.find_element_by_xpath(picture_xpath).send_keys("C:/Users/mumtaz/Desktop/python/selenium/cv&pic/PIC.jpg")
        self.driver.find_element_by_xpath(address_xpath).send_keys("Høje Gladsaxe 33")
        self.driver.find_element_by_xpath(postal_xpath).send_keys("2860")
        self.driver.find_element_by_xpath(city_xpath).send_keys("Copenhagen")
        self.driver.find_element_by_xpath(email_xpath).send_keys("mumtaz.maqsood@yahoo.com")
        self.driver.find_element_by_xpath(phone_xpath).send_keys("71425482")
        self.driver.find_element_by_xpath(mobile_xpath).send_keys("00000")
        self.driver.find_element_by_xpath(jobTitle_xpath).send_keys("Tester")
        self.driver.find_element_by_xpath(experience_xpath).send_keys("2 years")
        self.driver.find_element_by_xpath(education_xpath).send_keys("M.Sc Computer & Information System")
        self.driver.find_element_by_xpath(graduationYear_xpath).send_keys("4")
        self.driver.find_element_by_xpath(uploadCv_xpath).send_keys("C:/Users/mumtaz/Desktop/python/selenium/cv&pic/sm cv+cl.pdf")
        self.driver.find_element_by_xpath(term_xpath).click()
        self.driver.find_element_by_xpath(submitBtn_xpath).click()
        sleep(5)
    # ---------------------------------------------------------------------------------
    #  END TEST CASE 4.2
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # END TEST CASES 4  > MAIN MENU -- START : MAIN MENU -- CAREERS --> Sub Menus
    #                                           (OPEN POSITIONS, UNSOLICITED APPLICATION)
    # ---------------------------------------------------------------------------------



    # ---------------------------------------------------------------------------------
    # TEST CASES 5  > START : MAIN MENU -- NEWS
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 5.1 : CLICK ON MAIN_MENU "NEWS"
    # ---------------------------------------------------------------------------------

    def test_news_menu(self):
        newsMenu_xpath = self.driver.find_element_by_xpath("//span[contains(text(),'News')]")
        newsMenu_xpath.click()
        sleep(2)

    # ---------------------------------------------------------------------------------
    # END TEST CASES 5  > MAIN MENU -- NEWS
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # TEST CASES 6 > SEARCH MENU
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # START TEST CASE 6.1 : CLICK SEARCH ICON
    # ---------------------------------------------------------------------------------

    def test_search_menu(self):
        # searchMenu_xpath = self.driver.find_element_by_xpath("//a[@class ='fa fa-search']")
        searchMenu_xpath = self.driver.find_element_by_css_selector("#home1id")
        searchMenu_xpath.click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//div[@id='search_cls']//form[@id='searchform']").send_keys("hello")
        # print(searchMenu_xpath.is_enabled())
        #search_box.send_keys("hello world")
        sleep(10)

    # ---------------------------------------------------------------------------------
    # END TEST CASES 6  > MAIN MENU -- SEARCH ICON
    # ---------------------------------------------------------------------------------

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))
