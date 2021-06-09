import requests 
from bs4 import BeautifulSoup 

page =  requests.get("https://www.ndtv.com/coronavirus/india-covid-19-tracker")



src =  page.content

soup = BeautifulSoup(src, 'html.parser')

values =  soup.find_all("td")
states = soup.find_all("label")
cases =  soup.find_all("p" , class_ = "mid-wrap")

fh =  open("covid_data.csv" , "w")

j = 0
for i in states  :
    fh.write(i.get_text())
    fh.write(',')
    for k in range (4) :
        try :
            numbers = cases[j].get_text().split(" ")
            for h in numbers : 
                fh.write(h)
                fh.write(',')
            j += 1
        except :
            break 
    fh.write('\n')

fh.close()