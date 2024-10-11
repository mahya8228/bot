import requests
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=3*60*60)

@cached(cache)

def get_singer():
    url = "https://api.codebazan.ir/music"
    params = {
        "music" : music
    }
    response = requests.get(url=url, params=params)
    musics = requests.json(url).get("result")
    return musics
    if response.status_code != 200:
        return None
    return list(response.json())




if __name__ == "__main__":
     singer = input(":لطفا خواننده مورد نظر خود را وارد کنید")
     object = get_singer()
     print(f"اهنگ های خواننده مورد نظر شما:{object(url(singer))}")