import pytest
from selenium import webdriver


@pytest.fixture(autouse=True, scope='module')
def driverTest():

    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com/")
    print("Loading the driver")
    driver.implicitly_wait(30)
    status = driver.find_element_by_id("loginbutton").is_selected()
    print("I am printing")
    print(status)
    tt = driver.find_element_by_name("email").send_keys("deepti.madhuri@gmail.com")
    passw = driver.find_element_by_name("pass").send_keys("deepti1")


    lb = driver.find_element_by_id("loginbutton").click()

    return status

def test_login(self,driverTest):



    assert(self.status == True ,"Asserting please")

