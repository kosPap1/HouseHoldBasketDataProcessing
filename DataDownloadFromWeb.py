import time
from selenium import webdriver

# Insert the website URL
url = "https://e-katanalotis.gov.gr/householdBasket"

# Running the Driver for AB
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)
firstRowAB = driver.page_source

# Selecting the second row of data
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowAB = driver.page_source

# Writing the results to a file
f = open('sourceCodeAB1.txt', "a", encoding='utf-8')
f.write(firstRowAB)
f = open('sourceCodeAB1.txt', "a", encoding='utf-8')
f.write(secondRowAB)

# Running the driver for Bazaar

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to Baazar retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[2]")
clickable.click()

# retrieving data from first row
firstRowBazaar = driver.page_source

# retrieving data from second row
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowBazaar = driver.page_source

# Writing the results to a file
f = open('sourceCodeBazaar.txt', "a", encoding='utf-8')
f.write(firstRowBazaar)
f = open('sourceCodeBazaar.txt', "a", encoding='utf-8')
f.write(secondRowBazaar)



#running the driver for Galaxias


#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to Galaxias retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[3]")
clickable.click()

# retrieving data from first row
firstRowGalaxias = driver.page_source

# retrieving data from second row
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowGalaxias = driver.page_source

# Writing the results to a file
f = open('sourceCodeGalaxias.txt', "a", encoding='utf-8')
f.write(firstRowGalaxias)
f = open('sourceCodeGalaxias.txt', "a", encoding='utf-8')
f.write(secondRowGalaxias)



# running the driver for efood market

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to efood market retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[4]")
clickable.click()

# retrieving data from first row
firstRowEfood = driver.page_source

# retrieving data from second row
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowEfood = driver.page_source

# Writing the results to a file
f = open('sourceCodeEfood.txt', "a", encoding='utf-8')
f.write(firstRowEfood)
f = open('sourceCodeEfood.txt', "a", encoding='utf-8')
f.write(secondRowEfood)


# running the driver for eFreshgr market

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to eFreshgr market retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[5]")
clickable.click()

# retrieving data from first row
firstRoweFreshgr = driver.page_source

# retrieving data from second row
# No second row for eFreshgr

# Writing the results to a file
f = open('sourceCodeeFreshgr.txt', "a", encoding='utf-8')
f.write(firstRoweFreshgr)


# running the driver for discMarket market

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to discMarket market retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[6]")
clickable.click()

# retrieving data from first row
firstRowdiscMarket = driver.page_source

# retrieving data from second row
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowdiscMarket = driver.page_source

# Writing the results to a file
f = open('sourceCodediscMarket.txt', "a", encoding='utf-8')
f.write(firstRowdiscMarket)
f = open('sourceCodediscMarket.txt', "a", encoding='utf-8')
f.write(secondRowdiscMarket)


# running the driver for kritikos market

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to discMarket market retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[7]")
clickable.click()

# retrieving data from first row
firstRowkritikos = driver.page_source

# retrieving data from second row
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowkritikos = driver.page_source

# Writing the results to a file
f = open('sourceCodekritikos.txt', "a", encoding='utf-8')
f.write(firstRowkritikos)
f = open('sourceCodekritikos.txt', "a", encoding='utf-8')
f.write(secondRowkritikos)




# running the driver for Lidl market

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to discMarket market retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[8]")
clickable.click()

# retrieving data from first row
firstRowLidl = driver.page_source

# retrieving data from second row
#lidl has no second row

# Writing the results to a file
f = open('sourceCodeLidl.txt', "a", encoding='utf-8')
f.write(firstRowLidl)


#running the driver for masoutis market

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to discMarket market retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[9]")
clickable.click()

# retrieving data from first row
firstRowmasoutis = driver.page_source

# retrieving data from second row
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowmasoutis = driver.page_source

# Writing the results to a file
f = open('sourceCodeMasoutis.txt', "a", encoding='utf-8')
f.write(firstRowmasoutis)
f = open('sourceCodeMasoutis.txt', "a", encoding='utf-8')
f.write(secondRowmasoutis)


#running the driver for marketIn market

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to discMarket market retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[10]")
clickable.click()

# retrieving data from first row
firstRowmarketIn = driver.page_source

# retrieving data from second row
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowmarketIn = driver.page_source

# Writing the results to a file
f = open('sourceCodeMarketIn.txt', "a", encoding='utf-8')
f.write(firstRowmarketIn)
f = open('sourceCodeMarketIn.txt', "a", encoding='utf-8')
f.write(secondRowmarketIn)


#running the driver for MyMarket market

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to discMarket market retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[11]")
clickable.click()

# retrieving data from first row
firstRowMyMarket = driver.page_source

# retrieving data from second row
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowMyMarket = driver.page_source

# Writing the results to a file
f = open('sourceCodeMyMarket.txt', "a", encoding='utf-8')
f.write(firstRowMyMarket)
f = open('sourceCodeMyMarket.txt', "a", encoding='utf-8')
f.write(secondRowMyMarket)



#running the driver for Sklavenitis market

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to discMarket market retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[12]")
clickable.click()

# retrieving data from first row
firstRowSklavenitis = driver.page_source

# retrieving data from second row
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowSklavenitis = driver.page_source

# Writing the results to a file
f = open('sourceCodeSklavenitis.txt', "a", encoding='utf-8')
f.write(firstRowSklavenitis)
f = open('sourceCodeSklavenitis.txt', "a", encoding='utf-8')
f.write(secondRowSklavenitis)




#running the driver for Synka market

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to discMarket market retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[13]")
clickable.click()

# retrieving data from first row
firstRowSynka = driver.page_source

# retrieving data from second row
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowSynka = driver.page_source

# Writing the results to a file
f = open('sourceCodeSynka.txt', "a", encoding='utf-8')
f.write(firstRowSynka)
f = open('sourceCodeSynka.txt', "a", encoding='utf-8')
f.write(secondRowSynka)


#running the driver for Xalkiadakis market

#loading webpage
driver = webdriver.ChromiumEdge()
driver.get(url)
time.sleep(5)

#clicking to discMarket market retailer
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[14]")
clickable.click()

# retrieving data from first row
firstRowXalkiadakis = driver.page_source

# retrieving data from second row
clickable = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div[2]/div[2]/span[2]")
clickable.click()
time.sleep(2)
secondRowXalkiadakis = driver.page_source

# Writing the results to a file
f = open('sourceCodeXalkiadakis.txt', "a", encoding='utf-8')
f.write(firstRowXalkiadakis)
f = open('sourceCodeXalkiadakis.txt', "a", encoding='utf-8')
f.write(secondRowXalkiadakis)





