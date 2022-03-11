
print('''

▄▄▌ ▐ ▄▌ ▄▄▄· .▄▄ ·  ▄ .▄▪  ▄▄▄  ▪      ▄▄▄  ▄• ▄▌▄▄▌  ▄▄▄ .         ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
██· █▌▐█▐█ ▀█ ▐█ ▀. ██▪▐███ ▀▄ █·██     ▀▄ █·█▪██▌██•  ▀▄.▀·        ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·
██▪▐█▐▐▌▄█▀▀█ ▄▀▀▀█▄██▀▐█▐█·▐▀▀▄ ▐█·    ▐▀▀▄ █▌▐█▌██▪  ▐▀▀▪▄        ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
▐█▌██▐█▌▐█ ▪▐▌▐█▄▪▐███▌▐▀▐█▌▐█•█▌▐█▌    ▐█•█▌▐█▄█▌▐█▌▐▌▐█▄▄▌        ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
 ▀▀▀▀ ▀▪ ▀  ▀  ▀▀▀▀ ▀▀▀ ·▀▀▀.▀  ▀▀▀▀    .▀  ▀ ▀▀▀ .▀▀▀  ▀▀▀ (34)    ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀   
 (путь к выводу указывать в config.json)
 
  ''')

import requests, json, wget, os

url = 'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags=PASTETAG&limit=PASTELIMIT&json=1'

def convertFloatToDecimal(f=0.0, precision=2):
    return ("%." + str(precision) + "f") % f

# Input Block
limit = input('Limit [1 - 1000]: ')
tags = input('Tags: ')
dir_name = input('Folder name: ')

# Replaced TAGS, LIMIT.
url_replaced = url.replace('PASTETAG', tags)
limit_replaced = url_replaced.replace('PASTELIMIT', limit)

# REQUESTS block
r = requests.get(limit_replaced) # Получает лист
somelist = r.json()

# JSON block
f = open('config.json')
data = json.load(f)
path = data['path']

# Path block
#newPath = path.replace(os.sep, '/')
endPath = path.replace('REPLACE', dir_name)
os.makedirs(endPath, exist_ok=True)

# Cicle for
print('\n')

x = 0
for element in somelist:
    wget.download(element['file_url'], endPath)
    x += 1

# Script end
print('\n')
print(' Downloaded {} files'.format(x))