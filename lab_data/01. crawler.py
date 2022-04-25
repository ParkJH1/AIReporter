from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()
headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://news.naver.com/'
request = Request(url, headers=headers)
response = urlopen(request, context=context)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
results = soup.find_all('div', {'class', 'cjs_t'})
titles = []

for result in results:
    titles.append(result.text)

print(titles)
