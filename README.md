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
>>> 