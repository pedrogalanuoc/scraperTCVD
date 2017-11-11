import urllib.request
import urllib
import lxml
from lxml import html
import requests
import csv
import time


def download(url):
	print('Downloading:', url)
	response=urllib.request.urlopen(url)
	html=response.read()
	return html

webpage = requests.get("http://siq.uab.cat/siq_public/titulacions/").text
doc = html.fromstring(webpage)
link_list = doc.cssselect("a")

url_base = 'http://siq.uab.cat'

FIELDS = ('Tipus', 'Titulacio', 'Facultat', 'Credits', 'Solicituds', 'Primera_Opcio', 'Oferta', 'Matriculats',
 'Nous_Matriculats', 'Nota_Tall', 'Nota_Mitja', 'Nous_Homes', 'Nous_Dones', 'Rendiment', 'Rendiment_Nous', 'Mitjana_Credits',
 'Mitjana_Edat')
 

with open('data.csv','w', newline='') as file: 
 
	writer = csv.writer(file, delimiter=";")
	writer.writerow(FIELDS)
  
 
	for i in range(10,149):

		
		time.sleep(5)
		
		url_suf = link_list[i].attrib['href'].split(sep=';')[0]
			
		url = url_base+url_suf
		html = download(url)
		tree = lxml.html.fromstring(html)
	 
		row=[]
	 
		titulacio = tree.cssselect('div.subcl')
		if (titulacio == []): row.append("NA")
		else: row.append(titulacio[0].text_content().splitlines()[4].strip().split()[0])
			
		if (titulacio == []): row.append("NA")
		else: row.append(titulacio[0].text_content().splitlines()[4].strip())
	 
		if (titulacio == []): row.append("NA")
		else: row.append(titulacio[0].text_content().splitlines()[titulacio[0].text_content().splitlines().index("Centres on s'ofereix la titulació")+2].strip())
	 
		if (titulacio == []): row.append("NA")
		else: row.append(titulacio[0].text_content().splitlines()[titulacio[0].text_content().splitlines().index("Centres on s'ofereix la titulació")+9].strip().split()[1])
		 
		solicituds = tree.cssselect('tr.destacat > td.i_solicitud')
		if (solicituds == []): row.append("NA")
		else: row.append(solicituds[0].text_content())

		primeraopcio = tree.cssselect('tr.destacat > td.i_solicitud_1era')
		if (primeraopcio == []): row.append("NA")
		else: row.append(primeraopcio[0].text_content())

		oferta = tree.cssselect('tr.destacat > td.i_oferta')
		if (oferta == []): row.append("NA")
		else: row.append(oferta[0].text_content().strip())

		matriculats = tree.cssselect('tr.destacat > td.i_num_matriculats')
		if (matriculats == []): row.append("NA")
		else: row.append(matriculats[0].text_content())

		nousmatriculats = tree.cssselect('tr.destacat > td.i_nou_ingres')
		if (nousmatriculats == []): row.append("NA")
		else: row.append(nousmatriculats[0].text_content())

		notatall = tree.cssselect('tr.destacat > td.i_nota_tall')
		if (notatall == []): row.append("NA")
		else: row.append(notatall[0].text_content().strip())

		notamitja = tree.cssselect('tr.destacat > td.i_nota_mitja_acces')
		if (notamitja == []): row.append("NA")
		else: row.append(notamitja[0].text_content().strip())
		
		noushomes = tree.cssselect('table.taula_indicador')
		if not('2016' in noushomes[1].text_content().split()): row.append("NA")
		else: row.append(noushomes[1].text_content().split()[noushomes[1].text_content().split().index('2016')+3])

		if not('2016' in noushomes[1].text_content().split()): row.append("NA")
		else: row.append(noushomes[1].text_content().split()[noushomes[1].text_content().split().index('2016')+2])

		rendiment = tree.cssselect('tr.destacat > td.i_rendiment')
		if (rendiment == []): row.append("NA")
		else: row.append(rendiment[0].text_content().strip())

		rendimentnous = tree.cssselect('tr.destacat > td.i_rendiment_nou')
		if (rendimentnous == []): row.append("NA")
		else: row.append(rendimentnous[0].text_content().strip())

		mitjana_credits = tree.cssselect('table.taula_indicador')
		if not('2016' in mitjana_credits[4].text_content().split()): row.append("NA")
		else: row.append(mitjana_credits[4].text_content().split()[mitjana_credits[4].text_content().split().index('2016')+1])

		mitjana_edat = tree.cssselect('table.taula_indicador')
		if not('2016' in mitjana_edat[1].text_content().split()): row.append("NA")
		else: row.append(mitjana_edat[1].text_content().split()[mitjana_edat[1].text_content().split().index('2016')+1])
		

		writer.writerow(row)
		
		
	file.close()
	

print('Scraping completat')










 