from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element("#login_field")
username_box.send_keys("abcdef")


password_box = browser.find_element("#password")
password_box.send_keys("abcdef")
password_box.submit()


assert "abceef" in browser.page_source

profile_link = browser.find_element(".user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "abcdf" in link_label

browser.quit()

# read about waits and page objects in selenium
