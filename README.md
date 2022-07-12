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
...
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
.....
Other Man said:  Anyway, I did.
Man said:  You most certainly did not!
Other Man said:  Now let's get one thing quite clear: I most definitely told you!
Man said:  Oh no you didn't!
Other Man said:  Oh yes I did!
......
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


实例 sktch_try.py ，sketch.py 处理文件不存在的情况 
实际应用中sktch_try.py 更为灵活



"""4章 持久存储"""

实例 sketchChuli.py

import os

man=[]
other=[]
"""用异常 处理文件不存在"""
try:
	data=open('sketch.txt')
	"""用异常 处理错误的发生在预料中..."""
	for each_line in data:
	    try:
	        (role,line_spoken)=each_line.split(':',1)
	        """strip() 去除空白符"""
	        line_spoken=line_spoken.strip()
	        if role =='Man':
	        	man.append(line_spoken)
	       	elif role =='Other Man':
	       		other.append(line_spoken)        
	    except ValueError:
	    	pass
	data.close()
except IOError:
	print('The data file is missing!')

print(man)
print	(other)

"""运行结果"""
['Is this the right room for an argument?', "No you haven't!", 'When?', "No you didn't!", "You didn't!", 'You did not!', 'Ah! (taking out his wallet and paying) Just the five minutes.', 'You most certainly did not!', "Oh no you didn't!", "Oh no you didn't!", "Oh look, this isn't an argument!", "No it isn't!", "It's just contradiction!", 'It IS!', 'You just contradicted me!', 'You DID!', 'You did just then!', '(exasperated) Oh, this is futile!!', 'Yes it is!']
["I've told you once.", 'Yes I have.', 'Just now.', 'Yes I did!', "I'm telling you, I did!", "Oh I'm sorry, is this a five minute argument, or the full half hour?", 'Just the five minutes. Thank you.', 'Anyway, I did.', "Now let's get one thing quite clear: I most definitely told you!", 'Oh yes I did!', 'Oh yes I did!', 'Yes it is!', "No it isn't!", 'It is NOT!', "No I didn't!", 'No no no!', 'Nonsense!', "No it isn't!"]

***Repl Closed***
"""以写模式打开文件"""
 格式 out=open("data.out","w")

 out 数据对象
 data.out 所写文件的文件名
 w 要使用的访问模式 文件存在清空内容 追加一个文件 用a 完成写和读(不清除) 用w+ 

>>> out=open("data.out","w")
>>> print("Norwegian Blues stun easily.",file=out)
>>> out.close()
>>> 
"""写入磁盘文件"""
修改实例 sketchChuli.py print 部分为 运行后 磁盘多了 man_data.txt other_data.txt 

try:
	man_flie=open('man_data.txt','w')
	other_file=open('other_data.txt','w')
	print(man,file=man_flie)
	print	(other,file=other_file)
	man_flie.close()
	other_file.close()
except IOError:
	print("File error")
假设
try:   ok
	man_flie=open('man_data.txt','w') ok
	other_file=open('other_data.txt','w') ok
	print(man,file=man_flie) ok
	print	(other,file=other_file)  no ok"""有问题 后close()就不会运行"""
	man_flie.close() no 
	other_file.close() no
except IOError: ok
	print("File error")ok

"""finally: 不论什么情况，总会运行"""
try:
	man_flie=open('man_data.txt','w')
	other_file=open('other_data.txt','w')
	print(man,file=man_flie)
	print	(other,file=other_file)
except IOError:
	print("File error")
finally:
	man_flie.close()
	other_file.close()

"""试图打开不存在的文件missing.txt""''
>>> try:
	data=open('missing.txt')
	print(data.readline(),end='')
except IOError:
	print('File error')
finally:
	data.close()

	
File error
Traceback (most recent call last):
  File "<pyshell#19>", line 7, in <module>
    data.close()
NameError: name 'data' is not defined
>>> 
"""稍作修改 就不在报错 in  检测成员关系"""
>>> try:
	data=open('missing.txt')
	print(data.readline(),end='')
except IOError:
	print('File error')
finally:
	if 'data' in locals():
		data.close()

		
File error
>>> 
"""想要错误信息 再做修改后 又报错了 str"""
>>> try:
	data=open('missing.txt')
	print(data.readline(),end='')
except IOError as err:
	print('File error'+err) 
finally:
	if 'data' in locals():
		data.close()

		
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    data=open('missing.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#23>", line 5, in <module>
    print('File error'+err)
TypeError: can only concatenate str (not "FileNotFoundError") to str


"""再做修改 报错更详细"""
>>> try:
	data=open('missing.txt')
	print(data.readline(),end='')
except IOError as err:
	print('File error'+str(err)) 
finally:
	if 'data' in locals():
		data.close()

		
File error[Errno 2] No such file or directory: 'missing.txt'
>>> 

实例 sketchChuliwith.py  
import os

man=[]
other=[]
"""用异常 处理文件不存在"""
try:
	data=open('sketch.txt')
	"""用异常 处理错误的发生在预料中..."""
	for each_line in data:
	    try:
	        (role,line_spoken)=each_line.split(':',1)
	        """strip() 去除空白符"""
	        line_spoken=line_spoken.strip()
	        if role =='Man':
	        	man.append(line_spoken)
	       	elif role =='Other Man':
	       		other.append(line_spoken)        
	    except ValueError:
	    	pass
	data.close()
except IOError:
	print('The data file is missing!')
"""将文件命名为 man_data.txt和other_data.txt 用try/except 避免IOError"""
"""with 代替 finally with 完成了关闭文件工作"""
try:
	with open('man_data.txt','w') as man_flie, open('other_data.txt','w') as other_file:
		print(man,file=man_flie)
		print	(other,file=other_file)
except IOError as err:
	print("File error"+str(err))

文件的读取 
>>> with open("man_data.txt") as mdf:
	print(mdf.readline())

	
['Is this the right room for an argument?', "No you haven't!", 'When?', "No you didn't!", "You didn't!", 'You did not!', 'Ah! (taking out his wallet and paying) Just the five minutes.', 'You most certainly did not!', "Oh no you didn't!", "Oh no you didn't!", "Oh look, this isn't an argument!", "No it isn't!", "It's just contradiction!", 'It IS!', 'You just contradicted me!', 'You DID!', 'You did just then!', '(exasperated) Oh, this is futile!!', 'Yes it is!']



标准输出（Standard Output)  sys.stdout 

修改第二章print_lol()函数
源文件：
def print_lol(the_list,indent=False,level=0):
    for each_item in the_list:
        "检查是否为list 列表"
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
        	if indent:
	            for tab_stop in range(level):
	        	    print("\t",end='')
	        print(each_item)

修改：
import sys
def print_lol(the_list,indent=False,level=0, fn=sys.stdout):
    for each_item in the_list:
        "检查是否为list 列表"
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fn)
        else:
        	if indent:
	            for tab_stop in range(level):
	        	    print("\t",end='',file=fn)
	        print(each_item,file=fn)


"""引入print_lol()方法 修改后"""
import os
import nester

man=[]
other=[]
"""用异常 处理文件不存在"""
try:
	data=open('sketch.txt')
	"""用异常 处理错误的发生在预料中..."""
	for each_line in data:
	    try:
	        (role,line_spoken)=each_line.split(':',1)
	        """strip() 去除空白符"""
	        line_spoken=line_spoken.strip()
	        if role =='Man':
	        	man.append(line_spoken)
	       	elif role =='Other Man':
	       		other.append(line_spoken)        
	    except ValueError:
	    	pass
	data.close()
except IOError:
	print('The data file is missing!')
"""将文件命名为 man_data.txt和other_data.txt 用try/except 避免IOError"""
"""with 代替 finally with 完成了关闭文件工作"""
try:
	with open('man_data.txt','w') as man_flie, open('other_data.txt','w') as other_file:
		nester.print_lol(man,fn=man_flie)
		nester.print_lol(other,fn=other_file)
except IOError as err:
	print("File error"+str(err))
