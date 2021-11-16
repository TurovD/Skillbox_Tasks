def my_zip(*arg):
    arg = list(map(list, arg))
    try:
        yield tuple(map(lambda x : x.pop(0), arg))
        yield from my_zip(*arg)
    except:
        pass


for a in my_zip({'a':1,'b':2,'c':3},[1,2,3,4,5],[3,4,5],"asdf"):
    print(a)