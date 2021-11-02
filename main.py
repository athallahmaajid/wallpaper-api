from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {
        "message":"Check me on github https://github.com/athallahmaajid",
        "repo": "https://github.com/athallahmaajid/wallpaper-api",
        "docs":"/docs"
    }

@app.get('/wallpapers')
def get_api_by_category(category = None, page = 1, mobile = False):
    if category == None:
        response = requests.get("https://www.wallpaperflare.com/")
    else:
        if mobile:
            response = requests.get("https://www.wallpaperflare.com/search?wallpaper=" + category + "&mobile=ok" + "&page=",page)
        else:
            response = requests.get("https://www.wallpaperflare.com/search?wallpaper=" + category + "&page=",page)
    html = BeautifulSoup(response.text, "html.parser")
    wallpapers = []
    for i in html.find_all("img", {"class":"lazy"}):
        wallpapers.append(i['data-src'])
    return wallpapers

if __name__ == "__main__":
  uvicorn.run(app)
