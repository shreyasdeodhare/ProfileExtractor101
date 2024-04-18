from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import random
import csv
from time import sleep
options = Options()
user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',                       
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        ]
user_agents_cycle= iter(user_agents)


options.add_argument(f"--user-agent={next(user_agents_cycle)}")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--acceptInsecureCerts")  # Added to bypass SSL certificate errors


# driver = webdriver.Chrome(desired_capabilities=caps)


driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")


email = 'shreyasdeodhare18@gmail.com'
password = 'Shreyasd$1892001'
driver.get("https://www.linkedin.com/login")
sleep(2)  

email_input = driver.find_element(By.NAME, 'session_key')
email_input.send_keys(email)
password_input = driver.find_element(By.NAME, 'session_password')
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

sleep(5)
WebDriverWait(driver, 20).until(EC.url_contains("feed"))

search_query = "Python"
# driver.get(f"https://www.linkedin.com/search/results/people/?keywords={search_query}")

driver.get

sleep(2)  
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.TAG_NAME, 'div')))
div_ele=driver.find_elements(By.TAG_NAME,"div")

# print(div_ele)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.reusable-search__entity-result-list')))
search_results_ul = driver.find_elements(By.CSS_SELECTOR, ".reusable-search__entity-result-list")

# print(search_results_ul)

for search in search_results_ul: 
    
    people_list = search.find_elements(By.TAG_NAME, "li")
    print(people_list)
    with open("linkedin_profiles.csv", "a", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Name", "Job Title", "Skills", "Experience","Links"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for people in people_list:
          try:

             name = people.find_element(By.CSS_SELECTOR, "span[aria-hidden='true']").text
             
                

            # people.click()
             sleep(2)  

            # skills_section = driver.find_element(By.CLASS_NAME, "pv-skill-categories-section")
            # skills_list = skills_section.find_elements(By.CLASS_NAME, "pv-skill-category-entity__name")
            # skills = ", ".join([skill.text for skill in skills_list])

            # experience_section = driver.find_element(By.CLASS_NAME, "pv-profile-section__section-info")
            # experiences = experience_section.text
            # Task 3: Scrape the URLs of the profiles
            # profiles = driver.find_elements(By.CLASS_NAME, 'app-aware-link')
            # all_profile_URL = []
            # for profile in profiles:
            #      profile_ID = profile.get_attribute('href')
            #      profile_URL = "https://www.linkedin.com" + profile_ID
            #      if profile_URL not in all_profile_URL:
            #       all_profile_URL.append(profile_URL)


             writer.writerow({"Name": name})

             driver.back()
             sleep(2)  
          except Exception as e:
                 continue