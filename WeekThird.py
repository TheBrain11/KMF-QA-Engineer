from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from jira import JIRA
import time


def log_error_in_jira(summary, description):
    jira_options = {'server': 'https://websitefortests.atlassian.net'}
    jira = JIRA(options=jira_options, basic_auth=('test@gmail.com', 'testAPI'))

    try:
        new_issue = jira.create_issue(
            project='test',
            summary=summary,
            description=description,
            issuetype={'name': 'Task'}
        )
        print(f"Issue {new_issue} created in JIRA")
    except Exception as e:
        print(f"Failed to create issue in JIRA: {e}")



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:

    driver.get('https://kmf.kz/products/kmf-isker/')


    time.sleep(5)


    try:
        header = driver.find_element(By.XPATH, "//h1[contains(text(), 'KMF-ISKER')]")
        print("Header 'KMF-ISKER' found on the page.")
    except Exception as e:
        log_error_in_jira(
            summary='Header KMF-ISKER not found on the page',
            description=f"An error occurred while searching for the header: {str(e)}"
        )


    try:
        suitable_for_section = driver.find_element(By.XPATH, "//section[contains(text(), 'Подходит для')]")
        print("Section 'Подходит для' found on the page.")
    except Exception as e:
        log_error_in_jira(
            summary='Section Подходит для not found on the page',
            description=f"An error occurred while searching for the suitable for section: {str(e)}"
        )

    categories = [
        'Торговли',
        'Производства',
        'Услуг и сервиса',
        'Сельского хозяйства',
        'Для малого и среднего бизнеса',
        'Приобретения транспортного средства для бизнеса'
    ]

    for category in categories:
        try:
            category_element = driver.find_element(By.XPATH, f"//li[contains(text(), '{category}')]")
            print(f"Category '{category}' found on the page.")
        except Exception as e:
            log_error_in_jira(
                summary=f"Category {category} not found on the page",
                description=f"An error occurred while searching for the category '{category}': {str(e)}"
            )


finally:

    driver.quit()
