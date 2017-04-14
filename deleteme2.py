
import json, requests

response = requests.get('http://0.0.0.0:5000/getall')
data = json.loads(response.text)
name = data['5']['Name']
print(name)
urls = data['5']['MemeUrls'][0]
print(urls)
