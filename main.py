from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/")
def index():
    return {"message":"Check me on github https://github.com/athallahmaajid"}

@app.get('/wallpaper')
async def get_api_by_category(category: str, page: int = 0, mobile = False):
    if mobile:
        response = requests.get("https://www.wallpaperflare.com/search?wallpaper=" + category + "&mobile=ok" + "&page=",page)
    else:
        response = requests.get("https://www.wallpaperflare.com/search?wallpaper=" + category + "&page=",page)
    html = BeautifulSoup(response.text, "html.parser")
    wallpapers = []
    for i in html.find_all("img", {"class":"lazy"}):
        wallpapers.append(i['data-src'])
    return wallpapers
