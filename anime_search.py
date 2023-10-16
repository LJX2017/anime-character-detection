from image_downloader import download_keywords
from trainer import train
from trainer import predict
from fastcore.all import *
characters=['Mio', 'Azusa','Yui', 'Tsumugi','Ritsu']
path = Path('photos')
if not os.path.exists(path):
    download_keywords(path,characters, " from k-on anime solo photo")
if not os.path.exists(Path("anime learner.pkl")):
    train(path)
url = input("enter your image's url\n")

pred, idx, probs = predict(url)
print(f"This is {pred}'s picture, we are {float(probs[idx])*100:.0f}% sure")
