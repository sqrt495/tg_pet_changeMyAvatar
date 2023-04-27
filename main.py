from telethon import TelegramClient, sync
from config import *
import os
import random
import opencv

# client = TelegramClient('first_session', api_id, api_hash)
# client.start()

cwd = os.getcwd()
print(os.listdir(cwd+'/covers'))

get_random_covers_dir = random.choice(os.listdir(cwd+'/covers'))
if get_random_covers_dir == '.DS_Store' or 'hoaqin_tears_video':
       get_random_covers_dir = random.choice(os.listdir(cwd+'/covers'))

get_random_cover = random.choice(os.listdir(cwd+'/covers'+f'/{get_random_covers_dir}'))
print(get_random_cover)