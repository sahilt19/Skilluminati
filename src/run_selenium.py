from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def get_id(job_title):
    file = open("oes_ids.txt")
    for _line in file:
        line = _line.rstrip()
        link, job, oes_id = line.split(" | ")
        if job.lower() == job_title.lower():
            return oes_id
    return "oes151299.htm" # Return Other CS if not found

def get_link(job_title):
    file = open("oes_ids.txt")
    for _line in file:
        line = _line.rstrip()
        link, job, oes_id = line.split(" | ")
        if job.lower() == job_title.lower():
            return link
    return "https://www.bls.gov/oes/current/oes151299.htm" # Return Other CS if not found
    
def run_selenium(job_title):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("window-size=1920,1080")
    chrome_options.add_argument("start-maximized")
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    # For Windows
    # user_agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")
    # chrome_options.add_argument("--mute-audio")
    driver = webdriver.Chrome(options=chrome_options)
    # Access the website
    link = get_link(job_title)
    
    driver.get(link)
    tables = driver.find_elements(By.XPATH, "//table")
    # for table in tables:
    #     print(table.get_attribute("outerHTML"))
        
    maps = driver.find_elements(By.XPATH, "//img")
    # for img in maps:
    #     print(img.get_attribute("outerHTML"))
    return tables, maps

# Find job title
# Store a list of Job title - OES id
# using oes id search

