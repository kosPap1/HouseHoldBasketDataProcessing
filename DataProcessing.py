from bs4 import BeautifulSoup
import pandas as pd

# Code by SolumNox
# This part extracts the data from the HTML code
def cleaner(input):
    _ = str(input)
    _ = _.replace('<p class="householdBasket-category-name">', '')
    _ = _.replace('<p class="householdBasket-product-name">', '')

    _ = _.replace('<span class="householdBasket-products-price-number">', '')
    _ = _.replace('€<span class="unit">/τεμ.</span></span>', '')

    _ = _.replace('<span class="householdBasket-products-price-normalized-number">', '')
    _ = _.replace('€<span class="unit">/κιλό</span></span>', '')

    _ = _.replace('</p>', '')
    _ = _.replace('[', '')
    _ = _.replace(']', '')

    return _


# creating a vendors list
ventorsList = ['sourceCodeAB1.txt', 'sourceCodeBazaar.txt', 'sourceCodediscMarket.txt', 'sourceCodeEfood.txt', 'sourceCodeeFreshgr.txt',
            'sourceCodeGalaxias.txt', 'sourceCodekritikos.txt', 'sourceCodeLidl.txt', 'sourceCodeMarketIn.txt',
            'sourceCodeMasoutis.txt', 'sourceCodeMyMarket.txt', 'sourceCodeSklavenitis.txt', 'sourceCodeSynka.txt',
            'sourceCodeXalkiadakis.txt']

variables = ['AB', 'baazar', 'discMarket', 'Efood', 'eFresh', 'Galaxias', 'kritikos', 'lidl', 'marketIn', 'masoutis', 'myMarket', 'sklavenitis', 'synka', 'xalkiadakis']


# Combining the data into a single list
results = []
final = []
for i in range(len(ventorsList)):
    with open(ventorsList[i], 'r', encoding='utf-8') as f:
        html_string = f.read()
        soup = BeautifulSoup(html_string, 'html.parser')

        category_results = soup.find_all('p', class_="householdBasket-category-name")
        _ = cleaner(category_results)
        category = _.split(',')

        product_results = soup.find_all('p', class_="householdBasket-product-name")
        _ = cleaner(product_results)
        product_name = _.split(',')

        price_piece_results = soup.find_all('span', class_="householdBasket-products-price-number")
        _ = cleaner(price_piece_results)
        price_piece = [float(x) for x in _.split(',')]

        price_kilo_results = soup.find_all('span', class_="householdBasket-products-price-normalized-number")
        _ = cleaner(price_kilo_results)
        price_kilo = [float(x) for x in _.split(',')]

    for x in range(len(price_kilo)):
        temp = [product_name[x], price_piece[x], price_kilo[x]]
        results.append(temp)
    final.append(results)
    results=[]


# Converting the List to a DataFrame object

finalResult = pd.DataFrame()

for i in range(len(ventorsList)):
    df = pd.DataFrame(final[i])
    df.columns = ['Product', 'Price', 'Price per kilo']
    vendor = [str(variables[i])] * df.shape[0]  # do not change the shape 0
    df['Vendor'] = vendor
    finalResult = pd.concat([finalResult, df], axis=0, ignore_index=True )

print(finalResult)

# Saving the final result to a single csv file for further analysis
finalResult.to_csv('result.csv')




