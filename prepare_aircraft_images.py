from os import listdir
from os.path import isfile, join
import random
import shutil

source_dir = "/home/ubuntu/fastai-course/deeplearning1/nbs/data/fgvc-aircraft-2013b/data/images"
target_train_dir = "/home/ubuntu/fastai-course/deeplearning1/nbs/data/dogscats/train/airplanes"
target_valid_dir = "/home/ubuntu/fastai-course/deeplearning1/nbs/data/dogscats/valid/airplanes"

len_train_images = 9200
len_valid_images = 800

aircraft_images = [f for f in listdir(source_dir) if isfile(join(source_dir, f))]
random.shuffle(aircraft_images)
valid_images = aircraft_images[:len_valid_images]
train_images = aircraft_images[len_valid_images:]

for f in train_images:
	src = join(source_dir, f)
	dst = join(target_train_dir, ".".join(("airplane", f)))
	shutil.copy2(src, dst)

for f in valid_images:
	src = join(source_dir, f)
	dst = join(target_valid_dir, ".".join(("airplane", f)))
	shutil.copy2(src, dst)
