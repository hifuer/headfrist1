"""movies=["The Holy Grail",1975,"Tery Jones & Terry Gilliam",91,
        ["Graham Chapman",["Michael Palin","John Cleese",
                           "Terry Gilliam","Eric Idle","Terry Jones"]]]"""
"定义方法"
def print_lol(the_list):
    for each_item in the_list:
        "检查是否为list 列表"
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

"""print_lol(movies)"""
