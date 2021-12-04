# Sunglass Hut > Hidden API
# Tutorial from John Watson Rooney YouTube channel

import requests
import pandas as pd

url = "https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837"

results = []
for x in range(1, 13):
    querystring = {"isProductNeeded":"true","orderBy":["default","default","default"],"pageSize":"100","responseFormat":"json","isChanelCategory":"false","currency":"USD","pageView":"image","viewTaskName":"CategoryDisplayView","DM_PersistentCookieCreated":"true","beginIndex":"0","categoryId":"3074457345626651837","catalogId":"20602","langId":"-1","currentPage":[f"{x}",f"{x}"],"storeId":"10152","top":"Y"}

    headers = {
        "cookie": "aka-cc=US; aka-ct=SANTACLARITA; aka-zp=91350%2B91380%2B91382-91383%2B91390; ak_bmsc=637EE6BE7D70D262B87445589B9183A8~000000000000000000000000000000~YAAQKqbcF3UG0iR9AQAAL030gw7nK%2BM6L8FMCzXhrryotZ%2BdbKjgV2GuvMLPEHvVN6U%2FDB%2BIUqySIsPn6NHVGkmUg4yR6osMqfET9OF%2BTatEYpcV2urfoFv9XzKvOexf14ABcdymA20ZbT9yL2b2HLK%2F%2BJGvzi6tk42BwIBefMOWZqa9TsJlUF3m18IPpIzy93FqEq%2FK3h6M8OADcaf0EdUScPACE0Yl6egFBOcqaiVjVQcTqFAkosfdvStrkUTgJivt5p%2BboA8VKaPBq%2Fjdq7kecWZfsQJVqEbOjeglhZZN8LuEYkMzWcvyNN6zhcgGfKq7x5N00hePZmls1Oj6UXhqvnbMTdtwVc5XOrlKA0zTtNE3Rd2wovNisoqYaZaCMgR5MQhOkLPdf6amx7%2BnLQ%3D%3D; bm_sv=E979259BC02824F4197C0F1767CF2182~3sOOIyJjwwcHI9Rx7N5XlXJT0SrDAOu%2FmfQnYoz%2FGhBAFH%2FgCmLcOYVofSp3jififFJT0GhabSpYiDhgT7NVKiSVWiNHBYOkbaI14dw4qfx9Sq1CEeRsM2QV1LJcUjfd12NFZYf%2Fqv3sM4pnJNDMoN71wvx%2B4HEjej%2B%2BHCagkcU%3D; TS011f624f=015966d292553aa31da9f5632e7813e3dcbb7498055ba2c59dbe927a5da6139a54bb937fe295e5c392f025a455dd4f5bdf5bda3996",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    
    print(f'Getting products for page: {x}')
    for product in data['plpView']['products']['products']['product']: 
        results.append(product)

df = pd.json_normalize(results)
df.to_csv('Sunglass-Hut.csv')
print('Saved items to CSV file.')
