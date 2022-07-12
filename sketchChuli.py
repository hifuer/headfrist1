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