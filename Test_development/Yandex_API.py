import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = ''
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
def create_folder(folder_name):
    # responce = requests.put(f'{URL}?path={path}', headers=headers)
    params = {'path': folder_name}
    responce = requests.put(URL, params=params, headers=headers)
    return responce.status_code

def status_code(folder_name):
    params = {'path': folder_name}
    responce = requests.get(URL, params=params, headers=headers)
    if responce.status_code==200:
        return f'OK'

if __name__=='__main__':
    print(create_folder('STAR WARS'))
    print(status_code('STAR WARS'))