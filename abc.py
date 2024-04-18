# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import csv
# import random
# from time import sleep
# import logging
# class LinkedInScraper:
#     def __init__(self):
#         self.driver = self.setup_driver()
#         self.login()
#         self.search_query = "Python"
#         self.scrape_profiles()

#     def setup_driver(self):
#         options = Options()
#         options.add_argument("--ignore-certificate-errors")
#         options.add_argument("--ignore-ssl-errors")
#         options.add_argument("--acceptInsecureCerts")
#         options.add_argument(f"--user-agent={self.get_random_user_agent()}")
#         return webdriver.Chrome(options=options)

#     def get_random_user_agent(self):
#         user_agents = [
#             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
#             'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136',
#             'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
#             'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
#             'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
#         ]
#         return random.choice(user_agents)

#     def login(self):
#         email = 'shreyasdeodhare18@gmail.com'
#         password = 'Shreyasd$1892001'
#         self.driver.get("https://www.google.com/")
#         self.driver.get("https://www.linkedin.com/login")
#         email_input = self.driver.find_element(By.NAME, 'session_key')
#         email_input.send_keys(email)
#         password_input = self.driver.find_element(By.NAME, 'session_password')
#         password_input.send_keys(password)
#         password_input.send_keys(Keys.RETURN)
#         WebDriverWait(self.driver, 20).until(EC.url_contains("feed"))

#     def scrape_profiles(self):
#         self.driver.get(f"https://www.linkedin.com/search/results/people/?keywords={self.search_query}%20open%20to%20work")
#         WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.reusable-search__entity-result-list')))
#         search_results_ul = self.driver.find_element(By.CSS_SELECTOR, ".reusable-search__entity-result-list")
#         people_list = search_results_ul.find_elements(By.CLASS_NAME, "reusable-search__result-container")
#         with open("linkedin_profiles.csv", "a", newline="", encoding="utf-8") as csvfile:
#             fieldnames = ["Name", "Job Title", "Skills", "Experience", "Links"]
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()
#             for people in people_list:
#                 try:
#                     name = people.find_element(By.CSS_SELECTOR, "span[aria-hidden='true']").text
#                     link = people.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
#                     people.click()
#                     sleep(2)
#                     skills_section = self.driver.find_element(By.CLASS_NAME, "pvs-list")
#                     skills_list = skills_section.find_elements(By.TAG_NAME, "li")
#                     skills = ", ".join([skill.text for skill in skills_list])
#                     writer.writerow({"Name": name, "Skills": skills, "Links": link})
#                     logging.debug(self.driver.switch_to.window(self.driver.window_handles[0]))
#                     sleep(2)
#                 except Exception as e:
#                     continue

#     def close_driver(self):
#         self.driver.quit()

# if __name__ == "__main__":
#     scraper = LinkedInScraper()
#     scraper.close_driver()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import random
from time import sleep
import logging
class LinkedInScraper:
    def __init__(self):
        inp=input("Enter the skill to search :=")

        self.driver = self.setup_driver()
        self.login()
        self.search_query = inp
        self.scrape_profiles()

    def setup_driver(self):
        options = Options()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--acceptInsecureCerts")
        options.add_argument(f"--user-agent={self.get_random_user_agent()}")
        return webdriver.Chrome(options=options)

    def get_random_user_agent(self):
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        ]
        return random.choice(user_agents)

    def login(self):
        email = 'shreyasdeodhare18@gmail.com'
        password = 'Shreyasd$1892001'
        self.driver.get("https://www.google.com/")
        self.driver.get("https://www.linkedin.com/login")
        email_input = self.driver.find_element(By.NAME, 'session_key')
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.NAME, 'session_password')
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 20).until(EC.url_contains("feed"))

    def scrape_profiles(self):
        self.driver.get(f"https://www.linkedin.com/search/results/people/?keywords={self.search_query}%20open%20to%20work")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.reusable-search__entity-result-list')))
        search_results_ul = self.driver.find_element(By.CSS_SELECTOR, ".reusable-search__entity-result-list")
        people_list = search_results_ul.find_elements(By.CLASS_NAME, "reusable-search__result-container")
        with open("linkedin_profiles.csv", "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Name", "Job Title", "Skills", "Experience","Other", "Links"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for people in people_list:
                try:
                    name = people.find_element(By.CSS_SELECTOR, "span[aria-hidden='true']").text
                    link = people.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
                    self.scrape_profiles_data(name,link,writer)
                    
                except Exception as e:
                    logging.exception("Error occured while scraping profle")
    def scrape_profiles_data(self,name,link,writer):
         try:
            # Open profile in a new tab
            self.driver.execute_script(f"window.open('{link}','_blank');")
            sleep(3)  
            self.driver.switch_to.window(self.driver.window_handles[-1])
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pvs-list")))
            skills_section = self.driver.find_element(By.CLASS_NAME, "pvs-list")
            skills_list = skills_section.find_elements(By.TAG_NAME, "li")
            skills1=self.driver.find_elements(By.CSS_SELECTOR,"span[aria-hidden='true']")
            data=[s.text for s in skills1]
            div=skills_section.find_elements(By.CSS_SELECTOR,"div")
            data2=[di.text for di in div]
            
            for skills in skills_list: 
                skills = ", ".join([skill.text for skill in skills_list])
            # for s in skills1: 
            #     s1=", ".join(s.text for s in skills_
            writer.writerow({"Name": name, "Job Title": data, "Other":data2,"Skills":skills,"Links": link})
         except Exception as e:
            logging.exception("Error occurred while scraping profile:", e)
         finally:
            # Close the current tab
            self.driver.close()
            # Switch back to the main tab
            self.driver.switch_to.window(self.driver.window_handles[0])
            sleep(3)  # Allow some time before proceeding to the next profile
         

    def close_driver(self):
        self.driver.quit()

if __name__ == "__main__":
    scraper = LinkedInScraper()
    scraper.close_driver()
