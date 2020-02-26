import requests
baseUrl = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {'q': 'Cartago,CR', 'appid': 'YOUR API KEY FROM openweathermap.org/api_keys'}
response = requests.get(baseUrl, params=parameters)
print(response.content)