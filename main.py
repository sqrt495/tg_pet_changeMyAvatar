from telethon import TelegramClient, sync
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from config import *
import os
import random
import cv2
import matplotlib.pyplot as plt
import numpy as np
import time


client = TelegramClient('first_session', api_id, api_hash)
client.start()

# work with path
cwd = os.getcwd()
print(os.listdir(cwd+'/covers'))
dirs_list = os.listdir(cwd+'/covers')
get_random_covers_dir = random.choice(dirs_list)
if get_random_covers_dir == '.DS_Store' or 'hoaqin_tears_video':
       get_random_covers_dir = random.choice(os.listdir(cwd+'/covers'))

get_random_cover = random.choice(os.listdir(cwd+'/covers/'+get_random_covers_dir))

# read img
target_img = cv2.imread(cwd+'/covers/'+get_random_covers_dir+'/'+get_random_cover)
height, width, channels = target_img.shape

#Getting the bigger side of the image
s = max(target_img.shape[0:2])
#Creating a dark square with NUMPY
img_font = np.zeros((s,s,3),np.uint8)
#Getting the centering position
ax,ay = (s - target_img.shape[1])//2,(s - target_img.shape[0])//2
#Pasting the 'image' in a centering position
img_font[ay:target_img.shape[0]+ay,ax:ax+target_img.shape[1]] = target_img
# resize to 500x500
resized_img = cv2.resize(target_img,
                         dsize=(500, 500))
#Saving the image
path_to_save_resized_img = cwd + '/covers/' + get_random_covers_dir + '/' + get_random_cover + '_croped.jpg'
cv2.imwrite(path_to_save_resized_img,
            resized_img)

print(f'dir={get_random_covers_dir}',
      f'img={get_random_cover}',
      f'height={height}, width={width}',
      sep='\n')

print(path_to_save_resized_img)

time.sleep(3)

client(DeletePhotosRequest(client.get_profile_photos('me')))
file = client.upload_file(str(path_to_save_resized_img))
client(UploadProfilePhotoRequest(file))