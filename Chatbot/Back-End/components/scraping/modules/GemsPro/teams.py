from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# this GUID has a page with more txt sections
#GUID = "80befcce-cda0-4b35-9022-364ce2e1d1fe"

# this GUID has less txt sections so some elements won't exist
#GUID = '293e6863-c874-4e84-94df-233eface2fd0'
#DRIVER_PATH = "C:\webdriver\chromedriver.exe"
#driver = webdriver.Chrome(executable_path=DRIVER_PATH)

def scrape_team(GUID, driver):

    url = 'https://cg2019.gems.pro/Result/ShowTeam.aspx?Team_GUID=' + GUID + '&SetLanguage=en-CA'

    driver.get(url)
    txtEvent = ""
    txtTeamName = ""
    txtContingent = ""
    teamMembers = []
    teamMatches = []

    try:
        txtEvent = driver.find_element(By.ID, 'txtEventName')
        print("Team Event: " + txtEvent.text)
    except:
        print("No team event name.") 

    try:
        txtTeamName = driver.find_element(By.ID, 'txtName')
        print("Team Name: " + txtTeamName.text)
    except:
        print("No team Name.")

    try:
        txtContingent = driver.find_element(By.ID, 'txtContingent')
        print("Team Contingent: " + txtContingent.text)
    except:
        print("No team contingent.")

    try:
        txtFinalPosition = driver.find_element(By.ID, 'txtFinalPosition')
        print("Team Final Position: " + txtFinalPosition.text)
    except:
        print("No final position.")

    try:
        tblOdd = driver.find_elements(By.CLASS_NAME, "LM_ListDataRowOdd")
        for row in tblOdd:
            teamMatches.append(row.find_elements(By.CSS_SELECTOR, "td")[0].text)
            #for item in row.find_elements(By.CLASS_NAME, "LM_ListDataCell"):
                #print(item.text)
    except:
        print("No matches.")

    try:
        tblEven = driver.find_elements(By.CLASS_NAME, "LM_ListDataRowEven")
        for row in tblEven:
                teamMatches.append(row.find_elements(By.CSS_SELECTOR, "td")[0].text)
            #for item in row.find_elements(By.CLASS_NAME, "LM_ListDataCell"):
                #print(item.text)
    except:
        print("No even row matches.")

    try:
        tblTeamMembers = driver.find_element(By.CLASS_NAME, "LM_ShowTeamMemberTable")
        rowTeamMembers = tblTeamMembers.find_elements(By.CSS_SELECTOR, ".DataCell.InfoCell")
        for row in rowTeamMembers:
            teamMembers.append(row.find_elements(By.CSS_SELECTOR, "td")[1].text)

    except:
        print("No team table available.")

    try:
        print("Team Matches: ")
        joinedTeamMatches = ", ".join(teamMatches)
        print(joinedTeamMatches)
        joinedTeamMembers = ", ".join(teamMembers)
        print("Team Members: ")
        print(joinedTeamMembers)

    except:
        print("Unable to print.")

    finally:
        print("Scraped from: " + GUID)