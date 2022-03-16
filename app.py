import requests, json, wget, os

print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣶⣶⣶⣤⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠉⠉⠉⠉⠉⠙⢢⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢘⡉⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⢐⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠳⡦⣸⣷⣄⡀⢀⣀⡀⠀⠀⠀⡂⠀⠀- путь к выводу указывать в config.json
⠀⠀⠀⠀⠀⠀⠀⠀⡊⣿⣿⣿⣿⣯⡩⣉⠹⢷⢦⠁⠀⠀  CTRL + C - останавливает закачку
⠀⠀⠀⠀⠀⠀⠀⢰⠀⢻⣿⣿⣿⣿⣿⣿⣶⣶⡞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡌⠀⠀⢀⠉⠻⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⣀⠠⠤⠐⠚⠱⠀⠀⠀⠈⠀⠀⠀⠉⣻⠛⠋⠀⠀⠀⠀
⡇⠀⠀⡊⠠⠐⠁⠀⠀⠀⠀⢰⠀⢀⠆⠿⡀⠀⠀⠀⠀⠀
⡗⠒⠒⠀⠀⠀⠠⠤⢤⡀⠀⢸⠀⠘⠀⠀⢌⠑⢢⠀⠀⠀
⡇⠠⠀⠀⠀⠀⠀⠀⠀⠀⠑⢺⠀⠐⠀⠀⠂⠀⠀⠉⠒⠢⣄
⡇⠀⠀⠀⠀⠀⠀⠂⢰⠤⠀⠀⢦⠁⠀⠀⢂⠀⠀⠐⠄⠀⠠⠈⠉⠑⠦⡀
⡇⠀⡀⢀⠐⡀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠁⠄⠀⠀⠘
 ''')

def GetPath():
    f = open('config.json')
    data = json.load(f)
    path = data['path']
    return path

limit = input('Limit: ')
tags = input('Tags: ')
name = input('Folder name: ')

def CreateFolder():
    EndPath = GetPath() + '/' + name
    os.makedirs(EndPath, exist_ok=True)
    return EndPath

url = f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tags}&limit={limit}&json=1'

r = requests.get(url)
somelist = r.json()

x = 0
try: # CTRL + C = STOP
    while True:
        for element in somelist:
          count = len(somelist)
          wget.download(element['file_url'], CreateFolder())
          x += 1
          print('  | {}/{}'.format(x, count))
except KeyboardInterrupt:
    pass

# END
input('\nDownloaded {} files! Press ENTER to exit.'.format(x))