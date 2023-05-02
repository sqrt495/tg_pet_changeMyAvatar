from telethon import TelegramClient, sync
from config import *
import os
import random
import cv2
import matplotlib.pyplot as plt
import numpy as np

# client = TelegramClient('first_session', api_id, api_hash)
# client.start()

# work with path
cwd = os.getcwd()
print(os.listdir(cwd+'/covers'))

get_random_covers_dir = random.choice(os.listdir(cwd+'/covers'))
if get_random_covers_dir == '.DS_Store' or 'hoaqin_tears_video':
       get_random_covers_dir = random.choice(os.listdir(cwd+'/covers'))

get_random_cover = random.choice(os.listdir(cwd+'/covers'+f'/{get_random_covers_dir}'))

# read img
target_img = cv2.imread(cwd+'/covers/'+get_random_covers_dir+'/'+get_random_cover)
height, width, channels = target_img.shape

# check img center
true_height, true_width = False, False
if height > width:
       true_height == width
elif height < width:
       true_width = height
else: pass

#  crop

print(get_random_covers_dir,
      get_random_cover,
      height, width, channels,
      sep='\n')