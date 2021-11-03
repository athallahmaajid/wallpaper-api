from fastapi import FastAPI
from bs4 import BeautifulSoup
from requests import get
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
            wallpapers.append(i['src'].replace("300x168", "480x854"))
        else:
            wallpapers.append(i['src'].replace("300x168", "1920x1080"))
    return {"result":wallpapers}

@app.get('/wallpapers/search')
def get_wallpapers_by_query(query, page = 1, mobile = False):
    response = get(f"https://wallpaperscraft.com/search/?order=&page={page}&query={query}")
    html = BeautifulSoup(response.text, "html.parser")
    print(html.find("img", {"class":"wallpapers__image"}))
    wallpapers = []
    for i in html.find_all("img", {"class":"wallpapers__image"}):
        print(i)
        if mobile:
            wallpapers.append(i['src'].replace("300x168", "480x854"))
        else:
            wallpapers.append(i['src'].replace("300x168", "1920x1080"))
    return {"result":wallpapers}

if __name__ == "__main__":
  uvicorn.run(app)
