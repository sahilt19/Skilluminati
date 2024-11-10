from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re

chrome_options = Options()
# chrome_options.add_argument("--headless=new")
# chrome_options.add_argument("window-size=1920,1080")
# chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(options=chrome_options)
# Access the website
driver.get("https://www.bls.gov/oes/current/oes_stru.htm#00-0000")
link_tags = driver.find_elements(By.XPATH, "//a")
links=[]
jobs=[]
oes_ids=[]
for tag in link_tags:
    link = tag.get_attribute("href")
    if link and "current" in link and "stru" not in link:
        job = tag.get_attribute("innerHTML")
        job = job.replace('\n', ' ')
        job = re.sub(r'\s+', ' ', job)
        oes_id = link.split("/")[-1]
        
        links.append(link)
        jobs.append(job)
        oes_ids.append(oes_id)

file = open("oes_ids.txt", 'w')
for i in range(len(links)):
    # print(f"{links[i]} {jobs[i]} {oes_ids[i]}\n")
    file.write(f"{links[i]} | {jobs[i]} | {oes_ids[i]}\n")
print("File written successfully.")
file.close()
