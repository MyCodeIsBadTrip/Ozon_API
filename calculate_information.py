import requests
import json


if __name__ == '__main__':
	address = 'Санкт-Петербург, Петродворцовый район, посёлок Стрельна, Волхонское шоссе, 28'
	from_place_id = 8534308470000
	token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjQyMmNhZDNiLTc2MjMtNGZhYy1hMWEwLTIwZTQxMGQxNDRjMCIsInR5cCI6ImF0K2p3dCJ9.eyJuYmYiOjE2MzUyNDI2NDYsImV4cCI6MTYzNTMyOTA0NiwiaXNzIjoiaHR0cHM6Ly9hcGktc3RnLm96b25ydS5tZS9wcmluY2lwYWwtYXV0aC1hcGkiLCJjbGllbnRfaWQiOiJBcGlUZXN0XzExMTExMTExLTExMTEtMTExMS0xMTExLTExMTExMTExMTExMSIsIkxvem9uVXNlck5hbWUiOiJBcGlUZXN0IiwiTG96b25Db250cmFjdElkIjoiNzA1OTg4NTA1MTAwMCIsIkxvem9uUHJpbmNpcGFsSWQiOiI3NiIsImp0aSI6Ijk2QzJFRjhDMEFFMzE2QjI2RDhFQTJFM0Q1NEIwNzBEIiwiaWF0IjoxNjM1MjQyNjQ2LCJzY29wZSI6WyJkZWxpdmVyeS5wYXJhbXMuYXBpLnJlYWQiLCJwcmluY2lwYWwuaW50ZWdyYXRpb24uYXBpLmZ1bGwiLCJwcmluY2lwYWwucHJvZmlsZS5hcGkucmVhZC5hbGwiXX0.FHtehjBmkOmNXs_ON7xiRhKTqNd9O0vzQ-rqw3jXtddol1r0k0LWpCtEFFIP-GoypCTwiIQ0hsCte7NzF5HgYS5wZp2-_OLH3-qjkt_-UPO32kczprE9kf_6qIwnr-5pk9AM1GWo8omuzETiDrSIGfgcERCQGz2uvU8d74tWOmp9rCCGB8QCpJEuKTt6Gi5My_P1ZACnDMe8oaTg760UXX_TYOTDQji1PagbBp4LMLNcd_Kp2Yq558Se5bvlKJIRn4IxoNNcfl5Rg8VbZ_zkgMZnKtSXCFJ74DV1G7r8rInWykYSr6a69OQ8N5KzbZPviFmf91gdTLHBU-tsSTzPrw'

	# заголовки
	headers = dict()

	headers['Content-Type'] = 'application/json'
	headers['Authorization'] = 'Bearer ' + token

	# тело запроса
	body = dict()

	body['fromPlaceId'] = from_place_id
	body['destinationAddress'] = address

	# коробки
	body['packages'] = list()

	# первая коробка
	package1 = {
		'count': 1,
		'dimensions': {
			'weight': 1000,
			'length': 200,
			'height': 300,
			'width': 200
		},
		'price': 323
	}

	# вторая коробка
	package2 = {
		'count': 1,
		'dimensions': {
			'weight': 500,
			'length': 260,
			'height': 390,
			'width': 100
		},
		'price': 144
	}

	# добавляем коробки
	body['packages'].append(package1)
	body['packages'].append(package2)

	print(body)

	# запрос к API
	response = requests.post(
		url='https://api-stg.ozonru.me/principal-integration-api/v1/delivery/calculate/information',
	    data=json.dumps(body),
	    headers=headers
	)

	print(response.json())