import json
try:
    file = open('песни.txt', 'w', encoding='utf-8')
    file1 = open('MyData\YourLibrary.json', encoding='utf-8')
    data = json.load(file1)
    for tracks in data ["tracks"]:
        file.write(tracks["artist"] + ' ' + '-' + ' ' + tracks["track"] + '\n')
    print('выполнено')
except IOError:
    print ("Файл не найден")

file.close()
file1.close()
