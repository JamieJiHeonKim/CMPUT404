import requests

response = requests.get('http://raw.githubusercontent.com/JamieJiHeonKim/CMPUT404/master/main.py')

#print('Your IP is {0}'.format(response.json()['origin']))

#print(requests.__version__)

print(response.content)
