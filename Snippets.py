# import os
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager #controls automatic webdriver version managing
# from selenium.webdriver.chrome.service import Service #controls automatic browser closing after test run
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
# chrome_options = webdriver.ChromeOptions()

#--->>> Can use aliases to change import names
#from selenium.webdriver.support import expected_conditions as EC (now can call EC instead of expected_conditions)

#--->>> Page Load Strategy: "normal" by default - full page load. "eager" quicker and waits for DOM to load only
# chrome_options.page_load_strategy = "eager"

#--->>> chrome_options.add_argument("--headless") #--incognito, --ignore-certificate-errors, --disable-cache, --window-size=1920,1080

#--->>> Download web file locally. Change file download directory to local Pycharm folder. os.getcwd() gets a current working directory. Clicking download now will save
# a file to specified location, instead of saving it in the browser. Once downloaded the file can be worked with selenium
# prefs = {"download.default_directory" : f"{os.getcwd()}/FileDownloads"}
# chrome_options.add_experimental_option("prefs", prefs)

#--->>> Controls browser closing after test execution
# service = Service(executable_path=ChromeDriverManager().install())

#--->>> Pass browser settings before running a session
# driver = webdriver.Chrome(service=service, options=chrome_options)

#--->>> Upload file. Use send_keys() method. IMPORTANT: search for type=file on UI. That's where the file will be uploaded
# driver.find_element("xpath", "//input[@type='file']").send_keys(f"{os.getcwd()}/FileDownloads/fileName.png")

#--->>> Explicit Wait
# wait = WebDriverWait(driver, 10, poll_frequency=1)
# LOGIN_BUTTON = ("xpath", "//a[@title='My Account ']") using tuple to store locator
# wait.until(EC.visibility_of_element_located(LOGIN_BUTTON))
# driver.find_element(*LOGIN_BUTTON).click()

#--->>> 2 types of getting WebElement interacted with
# LOGIN_BUTTON = ("xpath", "//a[@title='My Account ']") WAY 1 as Tuple
# login_button = driver.find_element("xpath", "//a[@title='My Account ']") WAY 2 as WebElement
# driver.find_element(*LOGIN_BUTTON).click()
# login_button.click()

#--->>> For taking entire page screenshot (if no folder indicated, it will save in the current dir)
# driver.save_screenshot("FileDownloads/FirstScreen2.png")

#--->>> For taking specific WebElement screenshot
#element = driver.find_element("id", "exampleButton"), then element.screenshot("element_screenshot.png")

#--->>> WebDriver Mode and User Agent. Sometimes web apps know that automation is used to control the
# browser and might give you capchas, ask you to confirm you are human etc. To avoid that, use below 2 lines.
# One will remove the flag that the browser is run by automation. However sometimes a web app might also see that
# you have a user-agent that belongs to automation and do the same. So below 2 lines take care of that.
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
# Note: https://www.useragents.me/ and https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html https://prnt.sc/2OWEAU7N2JDo

#--->>> Working with Cookies is beneficial because I can skip login steps, have login sessions across multiple tests, modify, add or delete cookies.
# If cookies are saved, login steps such as finding elements and entering credentials can be omitted. Need to ---> import pickle <--- to save cookies into a file
# driver.get_cookie(name) - get cookie by name
# driver.get_cookies() - get all cookies (returns dictionary)
# driver.add_cookie({"name": "example", "value": "123"}) - add cookie
# driver.delete_cookie(name) - delete cookie by name
# driver.delete_all_cookies() - delete all cookies
# For example I do some action, like adding an item in amazon cart, then save all cookies from the website into a local file
# pickle.dump(driver.get_cookies(), open(os.getcwd() + "/FileDownloads/Cookies/cookies.pkl", "wb"))
# then delete all cookies driver.delete_all_cookies(), refresh page and see that the cart is empty
# then save all the cookies from local file into a variable
# cookie_from_file = pickle.load(open(os.getcwd() + "/FileDownloads/Cookies/cookies.pkl", "rb"))
# do a for loop to add cookies back, then refresh the page and see how cart got the item back
# for cookie in cookie_from_file:
# driver.add_cookie(cookie) and refresh page again

#--->>> pip freeze (shows the list of all installed packages in your current environment,
# along with their exact versions, in a format that’s ready to be saved to a requirements.txt file)
# pip freeze > requirements.txt
# then pip install -r requirements.txt

#--->>> To run tests with pytest, file name and every method has to start with test_methodName
#additional commands: pytest -v (prints test status and test name) and pytest -s (see print statements or input() prompts)

#--->>> Using Fixtures. Need to import pytest module. Then use: @pytest.fixture() and write a method for it
# Then simply pass methods name into another method name, that wants to use this particular fixture
# @pytest.fixture()
# def before1_fixture():
#     print("\nPrinting before 1")//use the fixture in any method by passing it to a method parameter
# def test_one(before1_fixture):
#     return True
# To selectively run a file or test: pytest -s -v test_Experimental.py::test_one (1st class name, then after :: method name)

#--->>> #


