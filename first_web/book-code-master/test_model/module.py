

class Mail:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        """ 登录 """
        frame1 = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/div[4]/div[1]/div/iframe')
        self.driver.switch_to.frame(frame1)
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys('username')
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys('password')
        self.driver.find_element_by_id("dologin").click()

    def logout(self):
        """ 退出 """
        self.driver.find_element_by_link_text("退出").click()
