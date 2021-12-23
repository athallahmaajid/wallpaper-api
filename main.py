from fastapi import FastAPI
from bs4 import BeautifulSoup
from requests import get
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
def get_wallpapers(mobile = False, page = 1):
    response = get(f"https://wallpaperscraft.com/all/page{page}")
    html = BeautifulSoup(response.text, "html.parser")
    wallpapers = []
    for i in html.find_all("img", {"class":"wallpapers__image"}):
        if mobile:
            wallpapers.append(i['src'].replace("300x168", "720x1280"))
        else:
            wallpapers.append(i['src'].replace("300x168", "1920x1080"))
    return {"result":wallpapers}

@app.get('/wallpapers/search')
def get_api_by_query(query, page = 1, mobile = False):
    wallpapers = []
    response = get("https://wall.alphacoders.com/search.php?search=" + query + "&page=" + str(page))
    html = BeautifulSoup(response.text, "html.parser")
    if mobile:
        if html.find_all("a", {"class":"custom-nav-tabs-element"}) != []:
            response = requests.get(html.find_all("a", {"class":"custom-nav-tabs-element"})[1]['href'] + "?page=" + str(page))
            html = BeautifulSoup(response.text, "html.parser")
        else:
            return {"result":wallpapers}
    for i in html.find_all("img", {"class":"img-responsive"}):
        if mobile:
            wallpapers.append(i['src'].replace("thumb-", "thumb-1920-"))
        else:
            wallpapers.append(i['src'].replace("thumbbig-", "thumb-1920-"))
    return {"result":wallpapers}

if __name__ == "__main__":
  uvicorn.run(app)
