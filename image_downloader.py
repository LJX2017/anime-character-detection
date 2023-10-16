# from fastcore.all import *
from fastai.vision.all import *
from duckduckgo_search import DDGS
import os
import shutil
def searchfor(term, count=30):
    print(f"Searching for {count} Pictures")
    with DDGS() as ddgs:
        results = ddgs.images(term, max_results=30)
        return L(results).itemgot('image')

def download_keywords(path,characters, addon=""):
    if os.path.exists(path):
        shutil.rmtree(path)
    urls = list()
    for c in characters:
        urls.append(list(searchfor(c + addon)))
    Download = dict(zip(characters, urls))
    for o in characters:
        target = path / o
        target.mkdir(parents=True, exist_ok=True)
        download_images(dest=target, urls=Download[o])
        resize_images(path / o, max_size=1000, dest=path / o)
    failed = verify_images(get_image_files(path))
    failed.map(Path.unlink)
