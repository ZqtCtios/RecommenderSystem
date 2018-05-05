import os
print("依次输入文件夹名，回车输入下一个文件夹，输入exit结束")
i=0
s=input('输入第{}个文件名：'.format(i))
path='./'
path=path+s
os.mkdir(path)
while True:
    i+=1
    s=input('输入第{}个文件名：'.format(i))
    if s=='exit':
        break
    path=path+'/'+s
    os.mkdir(path)
