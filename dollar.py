import requests 

#BTC, USD

def infos_values(moeda):
	#APi so funciona Com siglas em Maisuculo
	moeda_format = moeda.upper()
	sigla = moeda_format

	url= f'https://economia.awesomeapi.com.br/all/{moeda_format}'
	r = requests.get(url)
	
	print(f'Requisiçao status code: {r.status_code} ')

	infos = r.json()
	
	low_price = infos[sigla]['low']
	high_price = infos[sigla]['high']
	last_update = infos[sigla]['create_date']

	print(f'ultima atualizaçao: {last_update} ')
	print(f'Moeda analisada: {moeda_format} ')
	print(f'Alta da moeda: {high_price}R$ ')
	print(f'Baixa da moeda: {low_price}R$ ')

	return float(high_price)


infos_values('USD')
