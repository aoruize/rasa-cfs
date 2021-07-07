from bs4 import BeautifulSoup
import os
#import spacy


def search(searchPhrase):
  folders = [
    "biology", "chemistry", "documents", "firearms", "handbook",
    "toxicology"
  ]


  for f in folders:
    path = 'html_library/' + f

    for htmlFile in os.listdir(path):

      #print(htmlFile)
      filePath = path + '/' + htmlFile
      soup = BeautifulSoup(open(filePath), 'html.parser')

      h1s = soup.find_all('h1')
      h2s = soup.find_all('h2')
      h3s = soup.find_all('h3')
      h4s = soup.find_all('h4')
      #strongs = soup.find_all('strong')
      ps = soup.find_all('p')
      lis = soup.find_all('li')

      for h1 in h1s:
        if searchPhrase.lower() in h1.text.lower():
          print("RESULT FOUND IN H1 - " + filePath)
          print(h1.text)

      for h2 in h2s:
        if searchPhrase.lower() in h2.text.lower():
          print("RESULT FOUND IN H2 - " + filePath)
          print(h2.text)

      for h3 in h3s:
        if searchPhrase.lower() in h3.text.lower():
          print("RESULT FOUND IN H3 - " + filePath)
          print(h3.text)

      for h4 in h4s:
        if searchPhrase.lower() in h4.text.lower():
          print("RESULT FOUND IN H4 - " + filePath)
          print(h4.text)

      for p in ps:
        if searchPhrase.lower() in p.text.lower():
          print("RESULT FOUND IN P - " + filePath)
          print(p.text)
      
      for li in lis:
        if searchPhrase.lower() in li.text.lower():
          print("RESULT FOUND IN LI - " + filePath)
          print(li.text)



search("leak proof")
