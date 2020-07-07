# for i in range (1,100):
#     if (i % 5 != 0):
#         continue
#     print(i)


# 定义一个求两个数商和余数的方法 #方法定义
# def shang_yu (a,b):#a，b形参
#     print ("商",a // b)
#     print ("余",a % b)
# shang_yu(10,20)#10，20实参
# shang_yu(20,3)  #方法调用


# def shang_yu (a,b):#a，b形参
#    if(b == 0):
#        return None
#    else:
#        return (a // b,a % b)
# res = shang_yu(a = 20,b = 6)#按照关键字传参
# #res = shang_yu(20,6)#按照位置传参
# if res is None:
#    print ("参数错误")
# else:
#    print("商为：",res[0],"余数为：",res[1])


# def sm(a,b=2): #定义关键字形参，参数b设置默认值
#     return a+b
# print(sm(2))


# c = 2,3,4,5
# a,*b = (2,3,4,5)
# print(b)
#
# t = (1,2,3,4,5,6,7,8,9,77,88,99,44,55,66,11,22,33)
# s = 0
# for i in t:
#     s+=i


# def sum1(name,*args,**kwargs):# *args接收动态位置参数，**kwargs 接收动态关键字参数
#     print(kwargs)
#     print(name)
#     s = 0
#     for i in args:
#         s+=i
#     return s
# print(sum1(1,2,3,4,5,6,7,8,9,77,88,99,44,55,66,11,22,33))
# print(sum1(name="林先生"))


# class calc():#面向对象
#     a=None
#     b=None
#     res=None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)

# c = calc()

# c.input(10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()

# class calc():
#     res = None
#
#     def __init__(self,a,b): #魔法函数，类实例化的时候调用，又称构造方法
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a +self.b
#
#     def div(self):
#         self.res = self.a / self.b
#
#     def get_result(self):
#         print(self.res)
#
#
# c = calc(29,39)
# c.sum()
# c.get_result()
#
#
# # 类变量
# # 实例变量
# # 局部变量
#
# class calc():
#     res = None # 类的所有实例共享
#
#     def __init__(self,a,b): # 魔法函数，类实例化的时候调用，又称构造方法
#         self.a=a # 实例变量，只有当前对象可用
#         self.b=b
#         c = 10
#
#     def sum(self): # 实例方法
#         self.c = 10
#
#         self.res = self.a + self.b
#
#     def div(self):
#         self.res = self.a / self.b
#
#     def get_result(self):
#         print(self.res)
#
#     @classmethod
#     def get_res(cls): # 类方法定义：必须添加名字为@classmethod的装饰器，第一个参数名 cls cls代表当前类本身
#         print(cls.res)
#
#     @staticmethod
#     def static(): # 静态方法定义：必须使用@staticmethod装饰器，无默认参数
#         print("我是静态方法")
#
#
#
# c = calc(29,39) # 通过对象去操作实例变量
# c.a = 100
# print(c.a)
#
# calc.res = 1000 # 通过类名去操作类变量
# calc.get_res() # 类方法在使用的时候，通过类名调用。不需要实例化
#
# calc.static() # 通过类名调用

# for a in range(1,10):
#     for b in range(1,a+1):
#         print(b,"x",a,"=",b*a,end="\t")
#     print()


# l = [1,2,5,6,9,88,54,61,20,15,36,99,105,555,985,146,134,888,4646,2475,3586,7445,754,7512]
# length = len(l)
# for i in range(length-1,0,-1):#外层循环确定排好序的数据下标
#     for j in range(i):#遍历未排好序的列表
#         if (l[j] > l[j+1]):#判断相邻两个数据，前面的如果大于后面的，则交换两个数据的位置
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)
a = "我是day2中的a变量"

def name():
    print("我是day2中的name方法")

class Test():
    name="我是day2中的Test类"