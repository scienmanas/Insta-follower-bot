from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

USERNAME = "Your username"
PASSWORD = "Your password"
URL = "https://www.instagram.com/accounts/login/"

class Login() :
    def __init__(self,driver : WebDriver) -> None:
        self.driver = driver
        
    def logintoinsta(self) -> None:
        self.driver.get(URL)
        time.sleep(6)
        self.user_id = self.driver.find_element(By.NAME,'username')
        self.user_id.send_keys(USERNAME)
        self.pass_ = self.driver.find_element(By.NAME,'password')
        self.pass_.send_keys(PASSWORD)
        
        self.enter_button = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
        self.enter_button.click()
    
        self.not_now_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._ac8f div')))
        self.not_now_button.click()
        
    def followerBot(self,similar_account : str) :
        self.driver.get(f"https://www.instagram.com/{similar_account}/")
        self.driver.get(f"https://www.instagram.com/{similar_account}/followers/")
        
        self.dialog = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_aano')))
        self.start = 0
        try :
            for vev in range(3) :
                f_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div._aano button._acan._acap._acas._aj1-')
                self.length = len(f_buttons)
                for i in range(self.start,self.length):
                    try:
                        button = f_buttons[i]
                        button.click()
                        time.sleep(2)
                    except :
                        pass
                self.start = self.length
                self.driver.execute_script("arguments[0].scrollBy(0, 100)", self.dialog)
                time.sleep(2)
        except Exception as e :
            pass