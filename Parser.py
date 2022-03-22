import requests, json, wget, os

print('''
         ▄▄▌ ▐ ▄▌ ▄▄▄· .▄▄ ·  ▄ .▄▪  ▄▄▄  ▪      ▄▄▄  ▄• ▄▌▄▄▌  ▄▄▄ .          ▄▄▄· ▄▄▄· ▄▄▄  .▄▄ · ▄▄▄ .▄▄▄  
         ██· █▌▐█▐█ ▀█ ▐█ ▀. ██▪▐███ ▀▄ █·██     ▀▄ █·█▪██▌██•  ▀▄.▀·         ▐█ ▄█▐█ ▀█ ▀▄ █·▐█ ▀. ▀▄.▀·▀▄ █·
         ██▪▐█▐▐▌▄█▀▀█ ▄▀▀▀█▄██▀▐█▐█·▐▀▀▄ ▐█·    ▐▀▀▄ █▌▐█▌██▪  ▐▀▀▪▄          ██▀·▄█▀▀█ ▐▀▀▄ ▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ 
         ▐█▌██▐█▌▐█ ▪▐▌▐█▄▪▐███▌▐▀▐█▌▐█•█▌▐█▌    ▐█•█▌▐█▄█▌▐█▌▐▌▐█▄▄▌         ▐█▪·•▐█ ▪▐▌▐█•█▌▐█▄▪▐█▐█▄▄▌▐█•█▌
          ▀▀▀▀ ▀▪ ▀  ▀  ▀▀▀▀ ▀▀▀ ·▀▀▀.▀  ▀▀▀▀    .▀  ▀ ▀▀▀ .▀▀▀  ▀▀▀ (34.xxx) .▀    ▀  ▀ .▀  ▀ ▀▀▀▀  ▀▀▀ .▀  ▀

''')

limit = input(' Лимит: ')
tags = input(' Тэги: ')
name = input(' Название папки: ')

url = f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tags}&limit={limit}&json=1'

class Parser:

    def __init__(self):
        path_config = ('''
        {
            "path": "PASTHERE"
        }         
                    ''')
        try:
            config = 'config.json'
            f = open(config, 'r+')
        except FileNotFoundError:
            print('\n Не найден файл "config.json", создается новый.')
            f = open(config, 'w+')
            path_name = input(' Введите путь, где будут создаваться папки. \n (Пример: C:/Users/washiri/Desktop/So): ')
            path_r = path_config.replace("PASTHERE", path_name)
            f.write(path_r)
            pass

    def GetPath(self):
        f = open('config.json')
        data = json.load(f)
        return data['path']

    def CreateFolder(self):
        EndPath = self.GetPath() + '/' + name
        os.makedirs(EndPath, exist_ok=True)
        return EndPath

    def Download(self):
        r = requests.get(url)
        somelist = r.json()
        x = 0
        try: # CTRL + C = STOP
            while True:
                for element in somelist:
                    count = len(somelist)
                    wget.download(element['file_url'], self.CreateFolder())
                    x += 1
                    print('  | {}/{}'.format(x, count))
        except KeyboardInterrupt:
            print(f'\nОстановка. Скачано {x}/{count}')
            pass


if __name__ == '__main__':
    start = Parser()
    start.GetPath()
    start.CreateFolder()
    start.Download()
