import requests
key="e635e5dc5be3465c9be628f21737ebe1"
api_address="https://newsapi.org/v2/top-headlines?country=us&apiKey="+key

json_data=requests.get(api_address).json()

news=[]
def access_info():
    for i in range(5):
        news.append(" Number"+str(i+1)+",  " + json_data["articles"][i]["title"]+".  ")
    return news[:]
