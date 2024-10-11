"""
cron: 25 23 * * *
new Env('饿了么配置');
"""

import os
import glob

xsign = 'xsign.conf'  #文件名
text = 'http://192.168.2.2:9999/api/getXSign'
path = os.getcwd()  #当前文件夹路径
files = os.listdir(path) #获取目标文件夹中的所有文件名

for file_name in files:
    if file_name.endswith('.json'):
    file_path = os.path.join(path, file_name)
    os.remove(file_path)
	print('删除json文件成功')

if not os.path.exists(xsign):
    file = open(os.path.join(path, xsign), 'w') 
    file.write(text)
    file.close()
    print('创建xsign配置文件成功')
else:
    print('xsign配置文件已存在')