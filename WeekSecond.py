from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from jira import JIRA
import time


def log_error_in_jira(summary, description):
    jira_options = {'server': 'https://websitefortests.atlassian.net'}
    jira = JIRA(options=jira_options, basic_auth=('test@gmail.com', "testAPI"))

    new_issue = jira.create_issue(
        project='B4',
        summary=summary,
        description=description,
        issuetype={'name': 'Bug'}
    )
    print(f"Issue {new_issue} created in JIRA")



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:

    driver.get('https://kmf.kz/')


    time.sleep(5)


    try:

        logo = driver.find_element(By.XPATH, "//img[@alt='KMF']")
        print("Logo found on the homepage.")
    except Exception as e:
        log_error_in_jira(
            summary='Logo not found on KMF homepage',
            description=f"An error occurred while searching for the logo: {str(e)}"
        )

    try:

        products_section = driver.find_element(By.XPATH, "//section[@id='products']")
        print("Products section found on the homepage.")
    except Exception as e:
        log_error_in_jira(
            summary='Products section not found on KMF homepage',
            description=f"An error occurred while searching for the products section: {str(e)}"
        )



finally:

    driver.quit()
