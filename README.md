# headfrist1
head First python 

"""idle应用
Alt-P  前一个命令
Alt-N 后一个命令

Mac Centos7下
Ctrl-P  前一个命令
Ctrl-N 后一个命令

"""

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



"""第3章 文件与异常"""

"""导入标准os库"""
>>> import os

"""当前工作目录"""
>>> os.getcwd()
'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python39-32'

"""切换工作目录"""
>>> os.chdir('I:\\hf py1\\nester\\headfrist1')
>>> os.getcwd()
'I:\\hf py1\\nester\\headfrist1'
>>> 

"""打开文件 获取"一行数据"""
>>> data=open("sketch.txt")
>>> print(data.readline(),end='')
Man: Is this the right room for an argument?
>>> print(data.readline(),end='')
Other Man: I've told you once.
>>> 

"""使用seek() 方法返回文件起始位置，python文件也可用tell() """
>>> data.seek(0)
0
>>> for each_line in data:
	print(each_line,end="")

	
Man: Is this the right room for an argument?
Other Man: I've told you once.
Man: No you haven't!
Other Man: Yes I have.
Man: When?
Other Man: Just now.
Man: No you didn't!
Other Man: Yes I did!
Man: You didn't!

"""处理完，一定是将它关闭 """

>>> data.close()

"""文件出来split()"""
>>> data=open('sketch.txt')
>>> for each_line in data:
	(role,line_spoken)=each_line.split(':')
	print(role,end='')
	print(" said: ",end='')
	print(line_spoken,end='')

	
Man said:  Is this the right room for an argument?
Other Man said:  I've told you once.
Man said:  No you haven't!
Other Man said:  Yes I have.
Man said:  When?
Other Man said:  Just now.
Man said:  No you didn't!
Other Man said:  Yes I did!
Man said:  You didn't!
Other Man said:  I'm telling you, I did!
Man said:  You did not!
Other Man said:  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man said:  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man said:  Just the five minutes. Thank you.
Other Man said:  Anyway, I did.
Man said:  You most certainly did not!
Traceback (most recent call last):
  File "<pyshell#25>", line 2, in <module>
    (role,line_spoken)=each_line.split(':')
ValueError: too many values to unpack (expected 2)
"""上面处理文件出错 ，文件中用2个 ：号 """



"""请求帮助help() split()中还可传递 maxsplit=-1 参数""""
>>> help(each_line.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the words in the string, using sep as the delimiter string.
    
    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.
 

"""split(':',1) 参数修改""""
import os

data=open('sketch.txt')

for each_line in data:
    (role,line_spoken)=each_line.split(':',1)
    print(role,end='')
    print(" said: ",end='')
    print(line_spoken,end='')
data.close()

"""运行再次报错如下，数据中没有 ：号"""
================ RESTART: I:/hf py1/nester/headfrist1/sketch.py ================
Man said:  Is this the right room for an argument?
Other Man said:  I've told you once.
Man said:  No you haven't!
Other Man said:  Yes I have.
....
Man said:  Oh no you didn't!
Other Man said:  Oh yes I did!
Man said:  Oh look, this isn't an argument!
Traceback (most recent call last):
  File "I:/hf py1/nester/headfrist1/sketch.py", line 6, in <module>
    (role,line_spoken)=each_line.split(':',1)
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
"""find()方法 不包含返回-1， 包含返回正的索引值"""
>>> each_line="I tell you, there's no such thing as a flying circus."
>>> each_line.find(':')
-1
>>> each_line="I tell you: there's no such thing as a flying circus."
>>> each_line.find(':')
10
>>> 
"""添加if 判断语句 运行"""’

import os

data=open('sketch.txt')

for each_line in data:
    if not each_line.find(":")==-1:
        (role,line_spoken)=each_line.split(':',1)
        print(role,end='')
        print(" said: ",end='')
        print(line_spoken,end='')

data.close()

================ RESTART: I:/hf py1/nester/headfrist1/sketch.py ================
Man said:  Is this the right room for an argument?
Other Man said:  I've told you once.
Man said:  No you haven't!
Other Man said:  Yes I have.
Man said:  When?
Other Man said:  Just now.
Man said:  No you didn't!
Other Man said:  Yes I did!
Man said:  You didn't!
Other Man said:  I'm telling you, I did!
Man said:  You did not!
Other Man said:  Oh I'm sorry, is this a five minute argument, or the full half hour?
Man said:  Ah! (taking out his wallet and paying) Just the five minutes.
Other Man said:  Just the five minutes. Thank you.
Other Man said:  Anyway, I did.
Man said:  You most certainly did not!
Other Man said:  Now let's get one thing quite clear: I most definitely told you!
Man said:  Oh no you didn't!
Other Man said:  Oh yes I did!
Man said:  Oh no you didn't!
Other Man said:  Oh yes I did!
Man said:  Oh look, this isn't an argument!
Other Man said:  Yes it is!
Man said:  No it isn't!
Man said:  It's just contradiction!
Other Man said:  No it isn't!
Man said:  It IS!
Other Man said:  It is NOT!
Man said:  You just contradicted me!
Other Man said:  No I didn't!
Man said:  You DID!
Other Man said:  No no no!
Man said:  You did just then!
Other Man said:  Nonsense!
Man said:  (exasperated) Oh, this is futile!!
Other Man said:  No it isn't!
Man said:  Yes it is!
>>> 


"""修改文件格式 还会报错""""
""""""

try:
	代码
except:
	错误恢复代码

"""文件sketch_try.py""""
import os

data=open('sketch.txt')

for each_line in data:
    try:
        (role,line_spoken)=each_line.split(':',1)
        print(role,end='')
        print(" said: ",end='')
        print(line_spoken,end='')
    except:
    	pass
    	
data.close()


"""成功读取文件"""