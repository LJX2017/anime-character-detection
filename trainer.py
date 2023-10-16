from fastcore.all import *
from fastai.vision.all import *
from fastdownload import download_url
def train(path,steps = 20):
    dls = DataBlock(
        blocks=[ImageBlock, CategoryBlock],
        get_items=get_image_files,
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=[Resize(192, method='squish')]
    ).dataloaders(path, bs=32)
    learn = vision_learner(dls, resnet18, metrics=error_rate)
    learn.fine_tune(20)
    learn.export("anime learner.pkl")
def predict(url):
    path = Path("sample.jpg")
    download_url(url, path)
    learn = load_learner("anime learner.pkl")
    return learn.predict(PILImage.create("sample.jpg"))
