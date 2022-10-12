import os
import shutil

num=0
apath=r"/home/chenj0g/rgb_flow/rgbflow1"
bpath=r"/home/chenj0g/rgb_flow/rgbflow2"
cpath=r"/home/chenj0g/rgb_flow/rgbflow3"
dpath=r"/home/chenj0g/rgb_flow/rgbflow4"#abcdpath是你的1234文件夹
fivepath=r"/home/chenj0g/rgb_flow/video"#这里是你要经历筛选的文件夹
dirpath=r"/home/chenj0g/rgb_flow/queshi"#这里是你的目标路径文件夹
s=set()
abcd=['rgbflow1','rgbflow2','rgbflow3','rgbflow4']#这里放你那个1234的文件夹名字 比如你1是/home/dsadas，这里面的a就是dsadas
for curdir,roots,files in os.walk(apath):
    rootname=curdir.split('\\')[-1]
    s.add(rootname)
for curdir,roots,files in os.walk(bpath):
    rootname=curdir.split('\\')[-1]
    s.add(rootname)
for curdir,roots,files in os.walk(cpath):
    rootname=curdir.split('\\')[-1]
    s.add(rootname)
for curdir,roots,files in os.walk(dpath):
    rootname=curdir.split('\\')[-1]
    s.add(rootname)
for i in abcd:
    s.remove(i)
print(s)
for curdir,roots,files in os.walk(fivepath):
    for file in files:
        if file not in s:
            # print(movename)
            # print(dirpath+'\\'+file)#先输出 看下路径有没有问题
            # shutil.move(curdir+"\\"+file,dirpath+'/'+file)
