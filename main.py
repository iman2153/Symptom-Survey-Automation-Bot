from selenium import webdriver
from time import sleep
from login import username, password
chrome_driver_path = #should be location of chromedriver

driver = webdriver.Chrome(executable_path=chrome_driver_path)

class symptomSurveyBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def select_click(self, x_path):
        button = self.driver.find_element_by_xpath(x_path)
        button.click()

    def login(self):
        self.driver.get("https://campusready.ucdavis.edu/symptom-survey")
        complete_the_survey = self.driver.find_element_by_link_text("Complete the Survey")
        complete_the_survey.click()
        user_name = self.driver.find_element_by_xpath('//*[@id="username"]')
        user_name.send_keys(username)
        pass_word = self.driver.find_element_by_xpath('//*[@id="password"]')
        pass_word.send_keys(password)
        log_in = self.driver.find_element_by_xpath('//*[@id="submit"]')
        log_in.click()
        sleep(12)
        # complete symptom survey
        self.select_click('//*[@id="ctl03"]/div[2]/div/a')
        # continue
        self.select_click('//*[@id="mainbody"]/div[2]/div[1]/div/div[2]/a')
        # no1
        self.select_click('//*[@id="mainbody"]/main/form/div[2]/fieldset/div/div[2]/div')
        # no2
        self.select_click('//*[@id="mainbody"]/main/form/div[3]/fieldset/div/div[2]/div')
        # no3
        self.select_click('//*[@id="mainbody"]/main/form/div[4]/fieldset/div/div[2]/div')
        # no4
        self.select_click('//*[@id="mainbody"]/main/form/div[5]/fieldset/div/div[2]/div')
        # no5
        self.select_click('//*[@id="mainbody"]/main/form/div[6]/fieldset/div/div[2]/div')
        # yes
        self.select_click('//*[@id="mainbody"]/main/form/div[7]/fieldset/div')
        # continue2
        self.select_click('//*[@id="mainbody"]/footer/div/div[2]/input')
        self.driver.close()
