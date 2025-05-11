from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@given(u'launch the chrome browser')
def launchbrowser(context):
    s=Service("C:\pythondrivers\chromedriver-win64\chromedriver.exe")
    context.d=webdriver.Chrome(service=s)




@when(u'open orange hrm page')
def openHomepage(context):
    context.d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then(u'verify that logo present in the page')
def verifypage(context):
    a=context.d.find_element(By.XPATH,"//button[@type='submit']").is_displayed()
    assert a is True


@then(u'close the browser')
def closebrowser(context):
    context.d.close()
