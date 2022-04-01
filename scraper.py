#Import necessory libraries
import selenium
import pandas as pd
import time
import  requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(r"C:\Users\ABHINANDAN\Desktop\chromedriver.exe")
contract_urls = []
class Scrapper():
    url = "https://www.gov.uk/contracts-finder"
    #loading the page
    driver.get(url)
    time.sleep(2)

    #getting into the page containing contract details
    #Here we are fetching details of only active contract
    driver.find_element_by_xpath("//a[@class='gem-c-button govuk-button govuk-button--start gem-c-button--bottom-margin']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//button[@id='adv_search']").click()
    time.sleep(1)

    #creating an empty list for every contract urls
    
    
    #define function to get link for each contract
    def Contract_Url():
        for lnk in driver.find_elements_by_xpath("//a[@class='govuk-link search-result-rwh break-word']"):
            contract_urls.append(lnk.get_attribute('href'))
    Contract_Url()

    #lets iterate through all pages
    while True:
        try:
            driver.find_element_by_xpath("//li[@class='standard-paginate-next-box standard-paginate-next-icon']/a").click()
            time.sleep(1)
            Contract_Url()
        except NoSuchElementException:
            break
    

    #define empty lists for all details
    contract = []
    short_desc = []
    industry = []
    location = []
    contract_value = []
    reference = []
    published_date=[]
    closing_date = []
    closing_time = []
    start_date = []
    end_date=[]
    contract_type=[]
    proc_type=[]
    SME=[]
    VCSE = []
    description =[]
    links = []
    Buyer =[]
    address=[]
    telephone=[]
    email = []
    web_site=[]

    for lnk in contract_urls:
        driver.get(lnk)
        time.sleep(1)

        try:
            ctr=driver.find_element_by_xpath("//h1[@class='govuk-heading-l break-word']")
            contract.append(ctr.text)
        except NoSuchElementException:
            contract.append('-')
        try:
            s_des=driver.find_element_by_xpath("//h2[@class='breadcrumb-description']")
            short_desc.append(s_des.text)
        except NoSuchElementException:
            short_desc.append('-')
        try:
            ind=driver.find_element_by_xpath("//div[@class='content-block']/ul[1]")
            industry.append(ind.text.replace('\n',' '))
        except NoSuchElementException:
            industry.append('-')
        try:
            loc=driver.find_element_by_xpath("//strong[text()='Location of contract']//following::p")
            location.append(loc.text)
        except NoSuchElementException:
            location.append('-')
        try:
            val=driver.find_element_by_xpath("//strong[text()='Value of contract']//following::p")
            contract_value.append(val.text)
        except NoSuchElementException:
            contract_value.append('-')
        try:
            ref=driver.find_element_by_xpath("//strong[text()='Procurement reference']//following::p")
            reference.append(ref.text)
        except NoSuchElementException:
            reference.append('-')
        try:
            o_date=driver.find_element_by_xpath("//strong[text()='Published date']//following::p")
            published_date.append(o_date.text)
        except NoSuchElementException:
            published_date.append('-')
        try:
            c_date=driver.find_element_by_xpath("//strong[text()='Closing date']//following::p")
            closing_date.append(c_date.text)
        except NoSuchElementException:
            closing_date.append('-')    
        try:
            c_time=driver.find_element_by_xpath("//strong[text()='Closing time']//following::p")
            closing_time.append(c_time.text)
        except NoSuchElementException:
            closing_time.append('-')
        try:
            st_date=driver.find_element_by_xpath("//strong[text()='Contract start date']//following::p")
            start_date.append(st_date.text)
        except NoSuchElementException:
            start_date.append('-')
        try:
            ed_date=driver.find_element_by_xpath("//strong[text()='Contract end date']//following::p")
            end_date.append(st_date.text)
        except NoSuchElementException:
            end_date.append('-')
        try:
            typ=driver.find_element_by_xpath("//strong[text()='Contract type']//following::p")
            contract_type.append(typ.text)
        except NoSuchElementException:
            contract_type.append('-')
        try:
            typ=driver.find_element_by_xpath("//strong[text()='Procedure type']//following::p")
            proc_type.append(typ.text)
        except NoSuchElementException:
            proc_type.append('-')
        try:
            sme=driver.find_element_by_xpath("//strong[text()='Contract is suitable for SMEs?']//following::p")
            SME.append(sme.text)
        except NoSuchElementException:
            SME.append('-')
        try:
            vcse=driver.find_element_by_xpath("//strong[text()='Contract is suitable for VCSEs?']//following::p")
            VCSE.append(vcse.text)
        except NoSuchElementException:
            VCSE.append('-')
        try:
            desc=driver.find_element_by_xpath("//h3[text()='Description']//following::p[2]")
            description.append(desc.text)
        except NoSuchElementException:
            description.append('-')
        try:
            lnk=driver.find_element_by_xpath("//li[@class='list-no-bullets break-word']/a")
            links.append(lnk.get_attribute('href'))
        except NoSuchElementException:
            links.append('-')
        try:
            b_name=driver.find_element_by_xpath("//strong[text()='Contact name']/following::p")
            Buyer.append(b_name.text)
        except NoSuchElementException:
            Buyer.append('-')
        try:
            b_addr=driver.find_element_by_xpath("//strong[text()='Address']/following::p")
            address.append(b_addr.text)
        except NoSuchElementException:
            address.append('-')
        try:
            tel=driver.find_element_by_xpath("//strong[text()='Telephone']/following::p")
            telephone.append(tel.text)
        except NoSuchElementException:
            telephone.append('-')
        try:
            eml=driver.find_element_by_xpath("//strong[text()='Email']/following::p")
            email.append(eml.text)
        except NoSuchElementException:
            email.append('-')
        try:
            web=driver.find_element_by_xpath("//strong[text()='Website']/following::p/a")
            web_site.append(web.get_attribute('href'))
        except NoSuchElementException:
            web_site.append('-')

    #creating a dataframe
    data = list(zip(contract,short_desc,industry,location,contract_value,reference, published_date,closing_date,closing_time,start_date,end_date,contract_type,proc_type,SME,VCSE,description,links,Buyer ,address,telephone,email, web_site))
    df = pd.DataFrame(data, columns = ["Contract","Short Description","Industry","Location","Contract Value","Procurement reference", "Published date","Closing date","Closing time","Contract start date","Contract end date",
                                        "Contract type","Procedure type","Contract is suitable for SMEs?","Contract is suitable for VCSEs?","Description","Links","Contact name","Address","Telephone","Email","Website"])
    #saving the data into csv file
    df.to_csv(r"C:\Users\ABHINANDAN\Desktop\ Contract_Details.csv")