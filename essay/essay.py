#1'python 列表元素int和float相互转换
a=[[1,2],[3,4]]
'先转换为array'
import numpy as np
b=np.array([a],dtype='float32')
print(b)


#2'特征匹配中 kp=np.float32([kp.pt for kp in kp])


#3'闭包
'函数内的属性都有生命周期，都是在函数执行期间'
'函数内部对外部函数作用域里面变量的引用'

def func():
    a=1
    def func1(num):
        print(num+a,end='\ne\n')
    return func1
var=func()
print(var(3),end='\ne\n')


#4'装饰器
'不影响原有函数的功能，而且还能添加新功能'
def func1(func):
    def func2():
        print(1)
        return func()
    return func2
@func1
def myfun():
    print(2)
myfun()