from image_downloader import download_keywords
from trainer import *
from fastcore.all import *
import os
import platform
import subprocess
def print_results(result):
    pred, idx, probs = result
    print(f"This is {pred}'s picture, we are {float(probs[idx]) * 100:.0f}% sure")
characters=['Mio', 'Azusa','Yui', 'Tsumugi','Ritsu']
path = Path('photos')
if not os.path.exists(path):
    download_keywords(path,characters, " from k-on anime solo photo")
if not os.path.exists(Path("anime learner.pkl")):
    train(path)

picture_path = Path('Please drag and drop your picture here')

picture_path.mkdir(exist_ok=True)
if platform.system() == "Windows":
    os.startfile(picture_path)
elif platform.system() == "Darwin":
    subprocess.Popen(["open", picture_path])
else:
    subprocess.Popen(["xdg-open", picture_path])
while True:
    if len(os.listdir('Please drag and drop your picture here')) > 0:
        file_path = os.listdir('Please drag and drop your picture here')[0]
        if file_path[0] == '.':
            file_path = os.listdir('Please drag and drop your picture here')[1]

        print(file_path)
        print_results(file_predict(picture_path/file_path))
        shutil.rmtree(Path('Please drag and drop your picture here'))
        break
