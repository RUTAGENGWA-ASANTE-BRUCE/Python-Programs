from selenium import webdriver

class infow():
    def __init__(self):
          self.driver=webdriver.Chrome(executable_path="C://Users//stackOverFlow//Downloads//Compressed//chromedriver_win32_3//chromedriver.exe")
    def get_info(self,query):
      self.query=query
      self.driver.get(url='https://www.wikipedia.org/')
      search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
      search.send_keys(f"{self.query}")
      butt=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
      butt.click()
      paragraph=self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[1]')
      global p_salva
      p_salva=str(paragraph.get_text())
      