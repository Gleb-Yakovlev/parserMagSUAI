import requests
from bs4 import BeautifulSoup
import pandas

array = ["https://priem.guap.ru/mag/lists/list_1_514_1_1_3_f_2",
         "https://priem.guap.ru/mag/lists/list_1_23_1_1_3_f_2",
         "https://priem.guap.ru/mag/lists/list_1_505_1_1_3_f_2",
         "https://priem.guap.ru/mag/lists/list_1_506_1_1_3_f_2",
         "https://priem.guap.ru/mag/lists/list_1_25_1_1_3_f_2",
         "https://priem.guap.ru/mag/lists/list_1_103_1_1_3_f_2"]
excelName = "./mainExcel.xlsx"

mySnils = ""

data = []
for j in range(0, len(array)):
    print(array[j])
    req = requests.get(array[j])
    src = req.text
    
    soup = BeautifulSoup(src, 'lxml')
    
    head = soup.find_all("h3")
    
    table = soup.find_all("div", class_="table-responsive table")

    if table:
        tbody = 0
        for i in table:
            if i.find('tbody') is not None:
                tbody = i
        rows = tbody.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            data.append(cols)
    data.append(head[2])
    data.append(head[3])

df = pandas.DataFrame(data)
#df = df[(df[2]=="1")&(df[6]=="Да")]
#df = df[(df[1] == mySnils)]
df = df[(((df[2] == "1") | (df[2].isnull())) & ((df[6] == "Да")|(df[2].isnull()))) | (df[1] == mySnils)]
print(df)
df.to_excel(excelName)



