from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/Desktop-Computer-Motherboard-Diagnostic-Analyzer/dp/B072QSQQKT/ref=pd_sbs_3/137"
#            "-0981994-0229628?pd_rd_w=fi7XF&pf_rd_p=3676f086-9496-4fd7-8490-77cf7f43f846&pf_rd_r=GK9EE1E3HM88S0C4RPF0"
#            "&pd_rd_r=7e5c6df3-77ea-48b1-b963-f4c0087c408e&pd_rd_wg=wM32k&pd_rd_i=B072QSQQKT&psc=1")
driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

logo = driver.find_element_by_class_name("python-logo")
# print(logo.get_attribute("name"))

documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

### challenge ###
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)

# driver.close()
driver.quit()




