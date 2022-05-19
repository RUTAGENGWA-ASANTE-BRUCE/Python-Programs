from selenium import webdriver
paragraph =" "
class infow():
    def __init__(self):
      self.driver=webdriver.Chrome(executable_path="C://Users//pc//Downloads//Compressed//chromedriver_win32//chromedriver.exe")
    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query="+self.query)
        video=self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        video.click()
assist=infow()
assist.get_info("baby justin bieber")
