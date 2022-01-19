import requests
import pandas as pd
from bs4 import BeautifulSoup


url='https://en.wikipedia.org/wiki/List_of_Pakistan_ODI_cricketers'
city_page = requests.get(url).text
#print (city_page)

soup = BeautifulSoup(city_page,'lxml')
print(soup.title.text)

city_page_table = soup.find("table", attrs={"class", 'wikitable sortable'})
#print(city_page_table)

city_table_tr=city_page_table.find_all("tr")
#print(city_table_tr)

city_table_tr[2].text

city_table_td = city_table_tr[1].find_all("td")
#print(city_table_td[2].text)

Pakistan_cricketers_dataframe = pd.DataFrame()
#print(Pakistan_cricketers_dataframe)

for i in range(2,len(city_table_tr)):
    city_table_td = city_table_tr[i].find_all('td')

    Name = city_table_td[1].get_text().strip()
    Career = city_table_td[2].get_text().strip()
    Match = city_table_td[3].get_text().strip()

    Pakistan_cricketers_dataframe= Pakistan_cricketers_dataframe.append({'Name': Name,
                                                                        'Career': Career,
                                                                        'Match': Match}, ignore_index=True)
print(Pakistan_cricketers_dataframe)

#Pakistan_cricketers_dataframe.to_csv('Pakistan cricketers.csv')








