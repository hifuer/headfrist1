import os

"""用异常 处理文件不存在"""
try:
	data=open('sketch.txt')
	"""用异常 处理错误的发生在预料中..."""
	for each_line in data:
	    try:
	        (role,line_spoken)=each_line.split(':',1)
	        print(role,end='')
	        print(" said: ",end='')
	        print(line_spoken,end='')
	    except ValueError:
	    	pass
	data.close()
except IOError:
	print('The data file is missing!')
