import requests
key="e635e5dc5be3465c9be628f21737ebe1"
api_address="https://newsapi.org/v2/top-headlines/sources?apiKey="+key

json_data=requests.get(api_address).json()
#print(json_data)

jokes_url="https://official-joke-api.appspot.com/random_joke"
json_jokes=requests.get(jokes_url).json()
jokes=["",""]

jokes[0]=json_jokes["setup"]
jokes[1]=json_jokes["puncline"]