from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

companies_list = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://dev.swfinstitute.org/fund-manager-rankings/asset-manager")

table = driver.find_element(By.TAG_NAME, value="tbody")
rows = table.find_elements(By.TAG_NAME, value="tr")
for row in rows:
    company = row.find_element(By.TAG_NAME, value="a")
    company = company.text
    companies_list.append(company)

data = pd.DataFrame(companies_list)
# data.to_excel("Top 100 Asset Management Companies- Web Scraped.xlsx", index=False)

with pd.ExcelWriter(r"C:\Users\mathe\OneDrive\Desktop\Professional\Current Applications\Applications List.xlsx",
                    mode="a",
                    engine="openpyxl",
                    if_sheet_exists="new") as writer:
    data.to_excel(writer, sheet_name="Top 100 Asset Management Firms", index=False)


