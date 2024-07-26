import requests
from bs4 import BeautifulSoup
import pandas


IVTHead = "https://priem.guap.ru/mag/lists/list_1_514_1_1_3_f_2"
ISTHead = "https://priem.guap.ru/mag/lists/list_1_23_1_1_3_f_2"
Pribor11Head = "https://priem.guap.ru/mag/lists/list_1_505_1_1_3_f_2"
Pribor12Head = "https://priem.guap.ru/mag/lists/list_1_506_1_1_3_f_2"
ProgInshHead = "https://priem.guap.ru/mag/lists/list_1_25_1_1_3_f_2"
TTPHead = "https://priem.guap.ru/mag/lists/list_1_103_1_1_3_f_2"


IVTExcel = "./09.04.01 (1).xlsx"       
ISTExcel = "./09.04.02.xlsx"            
Pribor11Excel = "./12.04.01 (11).xlsx"  
Pribor12Excel = "./12.04.01 (12).xlsx" 
ProgInshExcel = "./09.04.04.xlsx"       
TTPExcel = "./23.04.01.xlsx"          

array = [[IVTHead, IVTExcel], 
         [ISTHead, ISTExcel], 
         [Pribor11Head, Pribor11Excel], 
         [Pribor12Head, Pribor12Excel], 
         [ProgInshHead, ProgInshExcel], 
         [TTPHead, TTPExcel]]

#excelArray = [IVTExcel, ISTExcel, Pribor11Excel, Pribor12Excel ,ProgInshExcel,TTPExcel]

for j in range(0, len(array)):
    print(array[j][0])
    print(array[j][1])
    req = requests.get(array[j][0])
    src = req.text
    
    soup = BeautifulSoup(src, 'lxml')
    
    head = soup.find_all("h3")
    
    table = soup.find_all("div", class_="table-responsive table")
    data = []

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
    data.append(head[3])
    
    df = pandas.DataFrame(data)
    #print(df[2])
    #df = df[df[2].isnull()]
    df = df[((df[2] == "1") | (df[2].isnull())) & ((df[6] == "Да")|(df[2].isnull()))]
    print(df)
    df.to_excel(str(array[j][1]))


# title = soup.title.string
# print(head[1])


# for row in data:
#     print(row)

# excelPath = "./test.xlsx"

# df = pandas.DataFrame(data)
# df.to_excel(excelPath)

