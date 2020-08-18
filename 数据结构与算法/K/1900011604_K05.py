import turtle as t

def f(x):  #斐波那契数列的第x项
    if x==1 or x==2:
        return 1
    else:
        return f(x-1)+f(x-2)
    
def rot(x):  #n阶卷
    if x >= 1:
        t.circle(4 * f(x), 90)
        rot(x-1)
    else:
        t.hideturtle()
        t.done()
rot(10)
