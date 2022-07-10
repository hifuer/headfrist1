# headfrist1
head First python 

"""创建列表""""
>>> cast=["Cleese","Palin","Jones","Idle"]
>>> print(cast)
['Cleese', 'Palin', 'Jones', 'Idle']
>>> print(len(cast))
4
>>> print(cast[1])
Palin

"""列表末尾添加数据"""
>>> cast.append("Gilliam")
>>> print(cast)
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']


"""列表末尾删除数据"""
>>> cast.pop()
'Gilliam'
>>> print(cast)
['Cleese', 'Palin', 'Jones', 'Idle']


"""列表末尾添加集合数据"""
>>> cast.extend(["Gilliam","Chapman"])
>>> print(cast)
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']


"""列表删除特定数据"""
>>> cast.remove("Chapman")
>>> cast
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']

"""列表特定位置添加数据"""
>>> cast.insert(0,"Chapman")
>>> cast
['Chapman', 'Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']


“""
1.创建文件夹 把模块拷贝到文件夹中
2.在文件夹中创建“setup.py”文件
3.构建一个发布文件
"""
$python setup.py sdist 

"""
4.将发布安装到python本地副本中
"""
$python setup.py install