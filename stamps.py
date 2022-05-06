from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import pickle

path = ("your_path") #enter path to the chrome driver. (driver version should match your chrome version)
url = 'https://registration.telangana.gov.in/stampStockPosition.htm'

driver = Chrome(path) #, options = chrome_options)
driver.get(url)

xps = {'district' : '//*[@id="districtCode"]', 'category':'//*[@id="category"]', 'denomination' : '//*[@id="denomination"]'}
output = {}

for k in xps:
    x = driver.find_element_by_xpath(xps[k])
    options = [i for i in x.find_elements_by_tag_name("option")]
    var = [element.get_attribute("text")  for element in options if element.get_attribute("text") != "Select..."]
    output[k] = var


data = {}

for a in output['district']:
    data[a] = {}
    for b in output['category']:
        data[a].update({b:[]})
        for c in output['denomination']:
            # print(a)
            # print(b)
            # print(c)  
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="districtCode"]'))).send_keys(a)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="category"]'))).send_keys(b)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="denomination"]'))).send_keys(c)  
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="stampStockRegister"]/div[3]/button[1]'))).click()
            xk = pd.read_html(driver.page_source)[0]
            if '------------ No Stamp Stock Found------------' in xk.values:
                data[a][b].append([c,'No Stamp Stock Found'])
            else:
                xk.columns = [xk.columns[i][0] for i in range(len(xk.columns))]
                xk = xk.iloc[:-1,:-1]
                xk.drop(['Sl.No'], axis = 1, inplace = True)
                data[a][b].append([c,xk])
            driver.get(url)



for m in data.keys():
    for i in data[m]:
        for j in data[m][i]:
            try:
                if 'No Stamp Stock Found' in j:
                    pass
            except ValueError:
                # print(m+"_"+('_').join(i.split(" "))+"_"+str(j[0])+".csv")
                j[1].to_csv(m+"_"+('_').join(i.split(" "))+"_"+str(j[0])+".csv", encoding = 'utf-8')
                # print('\n')
    

# =============================================================================
# 
# =============================================================================


"""


with open("your_path\dict_data.pickle", 'rb') as f:
    data = pickle.load(f)

data.pop('JAGTIAL')    
    
globals().update(data['HYDERABAD']['COURT FEE LABLES'])

x = %who DataFrame



data["ADILABAD"]['A.P.Adv WELFARE FUND STAMPS']
pd.DataFrame(data["ADILABAD"]['BROKER NOTE STAMPS'], columns = ['Denomination', 'Status'])


data["HYDERABAD"]['A.P.Adv WELFARE FUND STAMPS']
C = pd.DataFrame(data["HYDERABAD"]['A.P.Adv WELFARE FUND STAMPS'], columns = ['Denomination', 'Status'])





xk = pd.read_html(driver.page_source)[0].columns
xk.columns = [xk.columns[i][0] for i in range(len(xk.columns))]
xk = xk.iloc[:-1,:-1]
xk.drop(['Sl.No'], axis = 1, inplace = True)

for i in range(len(xk.columns)):
    print(xk.columns[i][0])

(pd.read_html(driver.page_source)[0].columns).to_flat_index()

xk.columns[]

pd.read_html(driver.page_source)[0]




pd.read_html(driver.page_source)[0]


pd.DataFrame(pd.read_html(driver.page_source)[0])

j = driver.find_element_by_xpath('//*[@id="wrapper1"]/div[2]/div[2]/table')


from bs4 import BeautifulSoup as bs

j = bs(driver.page_source,"html5lib")
f = j.findAll('table', attrs = {'class':'table table-bordered table-responsive'})
for i in f:
    h.html = i



for a in output['district']:
    dat[a] = {}
    for b in output['category']:
        dat[a].update({b:[]})
        for c in output['denomination']:
            print(a)
            print(b)
            print(c)  
            
            
            


for a in output['district']:
    data[a] = {}
    for b in output['category']:
        data[a].update({b:[]})
        # var =[]
        for c in output['denomination']:
            # var.append(c)            
            data[a][b].append([c,"j"])

"""

# =============================================================================
# 
# =============================================================================
