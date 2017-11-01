import sys
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

page = requests.get('http://xkcd.com/')
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')

n=int(sys.argv[1])
loc=sys.argv[2]
if not loc.endswith('/'):
	loc += '/'

for i in range(n):
	x=soup.find(id='comic').find('img')['src']
	link='http:'+x
	image=requests.get(link)
	img=Image.open(BytesIO(image.content))
	img.save(loc+x.split('/')[-1])
	temp=soup.findAll('ul', attrs={'class':'comicNav'})
	temp=temp[0].findAll('li')
	for t in temp:
		a=t.find('a')
		if a.has_attr('rel'):
			if(a['rel'][0] == 'prev'):
				temp1=a['href']
	page=requests.get('http://xkcd.com/'+temp1)
	contents=page.content
	soup=BeautifulSoup(contents,'html.parser')	