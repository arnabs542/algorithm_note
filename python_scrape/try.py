import requests

res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')

if str(res.status_code) == '200':
    with open('C:\\Users\\liuyu\Desktop\\2019_summer\\try.mp3', 'wb') as mp3:
        mp3.write(res.content)
        mp3.close()
    print('finished')
else:
    print('failed')
