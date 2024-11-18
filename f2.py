from bs4 import BeautifulSoup
import requests
import re

url1 = 'https://smart-lab.ru/forum/'
response1 = requests.get(url1)
#print(response1)
bs1 = BeautifulSoup(response1.text, 'lxml')
#print(bs)
temp0 = bs1.find_all(class_='kompanii_sector')
#print(temp)

sector = 'БАНКИ'#input()
company = 'ВТБ'#input()

'''for i in range(len(temp)):
    print('--------', (temp[i].find('h2')).text, i+1)
    temp0 = temp[i].find_all('a')
    for j in range(len(temp0)):
        print('----', temp0[j].text, j+1)'''


for i in range(len(temp0)):
    print('--------', (temp0[i].find('h2')).text, i+1)
    if (temp0[i].find('h2').text == sector):
        temp1 = temp0[i].find_all('a')
        for j in range(len(temp1)):
            print('------', temp1[j].text, j+1)
            if (temp1[j].text == company):
                print((temp1[j].get('href'))[7::])
                url2 = 'https://smart-lab.ru/forum/' + (temp1[j].get('href'))[7::]
                response2 = requests.get(url2)
                #print(response2)
                bs2 = BeautifulSoup(response2.text, 'lxml')
                #print(bs2)
                temp2 = bs2.find_all('tr')
                print(len(temp2), temp2[5])
                #for i in range(len(temp2)):
                #    print('----', (temp2[i].find('valueValue-l31H9iuA')).text, i+1)
                break
        break

#<div class="valueValue-l31H9iuA" style="color: rgb(242, 54, 69);">0.018690</div>
