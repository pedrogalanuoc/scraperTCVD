import urllib.request
import urllib
import lxml
from lxml import html
import requests
import csv


def download(url):
	print('Downloading:', url)
	response=urllib.request.urlopen(url)
	html=response.read()
	return html

webpage = requests.get("http://siq.uab.cat/siq_public/titulacions/").text
doc = html.fromstring(webpage)
link_list = doc.cssselect("a")

url_base = 'http://siq.uab.cat'

FIELDS = ('Titulacio', 'Facultat', 'Credits', 'Solicituds', 'Primera_Opcio', 'Oferta', 'Matriculats',
 'Nous_Matriculats', 'Nota_Tall', 'Nous_Homes', 'Nous_Dones', 'Rendiment', 'Rendiment_Nous', 'Mitjana_Credits',
 'Mitjana_Edat', 'Num_Homes', 'Num_Dones')
 

with open('data.csv','w') as file: 
 
	writer = csv.writer(file, delimiter=";")
	writer.writerow(FIELDS)
  
 
	for i in range(10,72):

		url_suf = link_list[i].attrib['href'].split(sep=';')[0]
			
		url = url_base+url_suf
		html = download(url)
		tree = lxml.html.fromstring(html)
	 
		row=[]
	 
		titulacio = tree.cssselect('div.subcl')[0]
		row.append(titulacio.text_content().splitlines()[4].strip())
	 
		row.append(titulacio.text_content().splitlines()[30].strip())
	 
		row.append(titulacio.text_content().splitlines()[37].strip().split()[1])
	 
		solicituds = tree.cssselect('tr.destacat > td.i_solicitud')[0]
		row.append(solicituds.text_content())

		primeraopcio = tree.cssselect('tr.destacat > td.i_solicitud_1era')[0]
		row.append(primeraopcio.text_content())

		oferta = tree.cssselect('tr.destacat > td.i_oferta')[0]
		row.append(oferta.text_content().strip())

		matriculats = tree.cssselect('tr.destacat > td.i_num_matriculats')[0]
		row.append(matriculats.text_content())

		nousmatriculats = tree.cssselect('tr.destacat > td.i_nou_ingres')[0]
		row.append(nousmatriculats.text_content())

		notatall = tree.cssselect('tr.destacat > td.i_nota_tall')[0]
		row.append(notatall.text_content().strip())

		noushomes = tree.cssselect('tr.destacat')[1]
		row.append(noushomes.text_content().split()[3])

		row.append(noushomes.text_content().split()[2])

		rendiment = tree.cssselect('tr.destacat > td.i_rendiment')[0]
		row.append(rendiment.text_content().strip())

		rendimentnous = tree.cssselect('tr.destacat > td.i_rendiment_nou')[0]
		row.append(rendimentnous.text_content().strip())

		mitjana_credits = tree.cssselect('tr.destacat')[5]
		row.append(mitjana_credits.text_content().split()[1])

		mitjana_edat = tree.cssselect('tr.destacat')[1]
		row.append(mitjana_edat.text_content().split()[1])

		row.append(mitjana_edat.text_content().split()[3])
		row.append(mitjana_edat.text_content().split()[2])

		writer.writerow(row)
		
	file.close()
	

print('Scraping completat')










 