import time
from selenium import webdriver

class SelScrable:
    def search(url):
        driver = webdriver.Chrome()
        driver.get(url)
        try:
            #time.sleep(10)
            pageBody = driver.find_element_by_css_selector('body').get_attribute("outerHTML")
        finally:
            driver.quit()
        return pageBody

if __name__=='__main__':
    test=SelScrable()
    test.page=search('https://r.onliner.by/ak/#bounds[lb][lat]=53.76819584019795&bounds[lb][long]=27.34085083007813&bounds[rt][lat]=54.02753677915656&bounds[rt][long]=27.78305053710938')
    
