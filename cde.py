# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# def linkedin_profile(query):
#  options=Options()
#  user_agents = [
#             'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
#             'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
#             'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
#             'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
#         ]
#  user_agents_cycle = iter(user_agents)

 
#  options.add_argument(f"--user-agent={next(user_agents_cycle)}")
#  options.add_argument("--ignore-certificate-errors")
#  options.add_argument("--ignore-ssl-errors")
#  options.add_argument("--acceptInsecureCerts")
    
#  browser = webdriver.Chrome(options=options)
#  browser.get('https://www.google.com/')
#  try:
#         browser.get(f"https://www.google.com/search?q={query}")
#         WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.g')))

#         google_results = browser.find_elements(By.CSS_SELECTOR, '.g')
#         linkedin_links = []

#         for result in google_results:
#             anchor = result.find_element(By.CSS_SELECTOR, 'a')
#             href = anchor.get_attribute('href')
#             if href and 'linkedin.com/in' in href:
#                 linkedin_links.append(href)

#         profiles = []
#         for link in linkedin_links:
#             profile = scrap_linkedin_profile(browser, link)
#             profiles.append(profile)

#         print(profiles)
#  except Exception as e:
#         print('Error during scraping:', e)
#  finally:
#         browser.quit()

# def scrap_linkedin_profile(browser, link):
#     browser.get(link)
#     WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.reusable-search__entity-result-list')))

#     name_elem = browser.find_element(By.CSS_SELECTOR, '.inline.t-24.t-black.t-normal.break-words')
#     name = name_elem.text.strip()

#     headline_elem = browser.find_element(By.CSS_SELECTOR, '.mt1.inline-block')
#     headline = headline_elem.text.strip()

#     location_elem = browser.find_element(By.CSS_SELECTOR, '.t-16.t-black.t-normal.inline-block')
#     location = location_elem.text.strip()

#     return {'name': name, 'headline': headline, 'location': location}

# linkedin_profile('site:linkedin.com/in/ AND "Python"')

from linkedin_api import Linkedin

try:
    api = Linkedin('shreyasdeodhare18@gmail.com', 'Shreyasd$1892001')

    # Send connection request to a given profile id, will return a boolean.
    api.add_connection('shreyas-deodhare')

    # Remove a connection with a given profile id, will return a boolean.

    # Fetch connection invitations for the currently logged in user with start and limit params.
    invitations = api.get_invitations(start=0, limit=3)
    print(invitations)

    # Unfollow a given profile id, will return a boolean.
    api.unfollow_entity('muhammedmoussa')

except:
  print("An exception occurred")