def makebold(func):
    def wrapped():
        return '<b>'+ func()+'</b>'
    return wrapped
def makespan(func):
    def wrapped():
        return "<span>"+func()+"</span>"
    return wrapped
@makebold
@makespan
def test1():
    return "hello world-1"
def test2():
    return "hello world-2"
print(test1())