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
