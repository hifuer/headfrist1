import sys

"""movies=["The Holy Grail",1975,"Tery Jones & Terry Gilliam",91,
        ["Graham Chapman",["Michael Palin","John Cleese",
                           "Terry Gilliam","Eric Idle","Terry Jones"]]]"""
"定义方法 indent=False 缺省值"

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

"""print_lol(movies,True,1)"""
