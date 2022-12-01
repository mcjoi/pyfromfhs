## parser.py
import requests
from bs4 import BeautifulSoup


range = range(1,528)
mytitles = []

f = open("myblog.txt", 'w')

for i in range :
  ## HTTP GET Request
  req = requests.get('https://sunnybong.tistory.com/' + str(i))
  ## HTML 소스 가져오기
  html = req.text  
  soup = BeautifulSoup(html, 'html.parser')
  # print(soup)
  # title = soup.select("title")
  title1 = soup.find('title')
  title2 = str(title1)
  title2 = title2.replace('<title>', '')
  title2 = title2.replace('</title>', '')

  index = str(i)
  
  if len(index) == 2 : 
    index = '0' + index
  elif len(index) == 1 :
    index = '00' + index
  else : 
    index = index

    
  f.write( index + ' ' + title2 + '\n')
  
  
  # mytitles.append(title)

f.close()

# for j in mytitles :
  
#   print(j[0])
  


# for key in my_titles:        
#     if index >= 20:
#         break