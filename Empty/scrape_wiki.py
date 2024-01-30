from bs4 import BeautifulSoup as bs
import requests


ENCODING = "utf-8"

path = "chromedriver_win32"

resp = requests.get("https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27de_yasama")

# gets the year information for each Legislative Term 
# and writes the information into a .txt file

soup = bs(resp.text, "html.parser")
counter = 1
table = soup.find("table", {"class" : "wikitable"})
table = table.find("tbody")
mylist = list(table.find_all("tr"))
out_file = open("year_assembly_no.txt", "a", encoding=ENCODING)
for row in mylist:
    try: 
        target = list(row.find_all("td"))[1].text.strip("*")
        if (target[:4] == "TBMM"): # if the row contains Term information
            date = list(row.find_all("td"))[2].text
            year = date.split(" ")[2]
            print(target, year)
            counter += 1
            tbw = target.split(" ")[1][:-1] + " " + year + "\n"
            out_file.write(tbw)
    except:
        pass



    
