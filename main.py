import promptlib
import requests
import wget 
import json 
import os

print('''
▄▄▌ ▐ ▄▌ ▄▄▄· .▄▄ ·  ▄ .▄▪  ▄▄▄  ▪  .▄▄ ·      ▄▄▄· ▄▄▄· ▄▄▄  .▄▄ · ▄▄▄ .▄▄▄  
██· █▌▐█▐█ ▀█ ▐█ ▀. ██▪▐███ ▀▄ █·██ ▐█ ▀.     ▐█ ▄█▐█ ▀█ ▀▄ █·▐█ ▀. ▀▄.▀·▀▄ █·
██▪▐█▐▐▌▄█▀▀█ ▄▀▀▀█▄██▀▐█▐█·▐▀▀▄ ▐█·▄▀▀▀█▄     ██▀·▄█▀▀█ ▐▀▀▄ ▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ 
▐█▌██▐█▌▐█ ▪▐▌▐█▄▪▐███▌▐▀▐█▌▐█•█▌▐█▌▐█▄▪▐█    ▐█▪·•▐█ ▪▐▌▐█•█▌▐█▄▪▐█▐█▄▄▌▐█•█▌
 ▀▀▀▀ ▀▪ ▀  ▀  ▀▀▀▀ ▀▀▀ ·▀▀▀.▀  ▀▀▀▀ ▀▀▀▀     .▀    ▀  ▀ .▀  ▀ ▀▀▀▀  ▀▀▀ .▀  ▀''')


class Parser:

    def __init__(self):
    # Checks config file, if not exist create a new one 
        try:
            config = 'config.json'
            f = open(config, 'r+')
        
        except FileNotFoundError:
            print('''
>>> Config file is not exist.
>>> Set the path, where folders will be contained.''')
            prompter = promptlib.Files()
            directory = prompter.dir()
            data = {'path': directory}
            with open(config, 'w') as outfile:
                json.dump(data, outfile)
                print(f'''>>> Done! {dir}''')

    def Path(self):
        f = open('config.json')
        data = json.load(f)
        return data['path']

    def Folder(self):
        EndPath = self.Path() + '/' + folder_name
        os.makedirs(EndPath, exist_ok=True)
        return EndPath

    def Download(self):
        r = requests.get(url_a)
        somelist = r.json()
        x = 0
        i = 0
        try: 
            for element in somelist:
                count = len(somelist)
                wget.download(element['file_url'], self.Folder())
                x += 1
                i += 1
                print(f'  | {x}/{count}')
        except KeyboardInterrupt: # CTRL + C = STOP
            print(f'\nОстановка. Скачано {x}/{count}')

if __name__  == '__main__':
    Parser().Path()
    folder_name = input('\nFolder name: ')
    Parser().Folder()
    tags = input('Tags: ')
    limit = input('Limit: ')
    url_a = f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tags}&limit={limit}&json=1'
    Parser().Download()
