from bs4 import BeautifulSoup
import requests

response = requests.get("https://en.wikipedia.org/wiki/PK-7_Swat-V")
#print(response)
#print(response.text)

contents = response.text
#https://news.ycombinator.com/
#make a list of all headings, links

'''file = open("index.html")
contents = file.read()
#print(contents)
file.close()

#import lxml(install package ).....if required
soup = BeautifulSoup(contents, "html.parser")'''

#print(soup.prettify())
#print(soup.title)
#print(soup.a)
#print(soup.h1)
#print(soup.find_all(name = "a"))#p, etc

#print(soup.find(name = "a").get("href"))#p, etc

"""list = soup.find_all(name = "a")
for link in list :
    print(link)"""
    
'''list = soup.find_all(name = "a")
for link in list :
    print(link.get("href"))'''

'''first_heading = soup.find(name = "h1")
print(first_heading.getText())'''

#print(soup.h1.text)

'''first_heading = soup.find(class_ = "my-class")
print(first_heading.getText())'''

'''first_heading = soup.select(selector_ = "div .my-class")
print(first_heading)'''

